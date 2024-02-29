from functools import partial
import urllib.request
import logging, random, requests
from bs4 import BeautifulSoup  
from tqdm import tqdm
import os,shutil, multiprocessing, time
import subprocess,logging, tempfile
import magic, zipfile, tarfile, rarfile
from tqdm.contrib.concurrent import process_map

# Create log file
def create_log(log_path: str):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                        datefmt='%a %d %b %Y %H:%M:%S',
                        filename=log_path)
    formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s')
    # 将日志写入文件并输出到控制台
    streamlog = logging.StreamHandler()
    streamlog.setFormatter(formatter)
    streamlog.setLevel(logging.INFO)
    # 获取根日志记录器并设置格式
    root_logger = logging.getLogger('')
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(streamlog)
    return

# Get links to papers
def crawl_arxiv(identity: str,year: int, num_page: int, pages: int):
    # 爬取的页面
    url = f'https://arxiv.org/list/{identity}/{str(year)}?skip={pages * num_page}&show={str(num_page)}'
    headers = {
        "Referer": url,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)\
                  Version/16.1 Safari/605.1.15',
        'Accept-Encoding': '*/*',
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = response.apparent_encoding
        html_content = response.text
        status_code = response.status_code
        if status_code != 200:
            logging.error(f"Request to {url} failed with status code {status_code}")
            return []
    except Exception as e:
        logging.error(f"An error occurred while fetching {url}: {str(e)}")
        return []

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find information on all papers on the page
    target = soup.find_all('a', attrs={'href': True, 'title': 'Abstract'})
    
    # Get the link to the paper
    arxiv_list = [a.text.replace("arXiv:", "") if a.text.startswith("arXiv:") else a.text for a in target if a.text]
    
    # Random dormancy
    time.sleep(random.randint(5, 8))

    return arxiv_list

# Use the information obtained from the paper to download Tex files
def download_tex(isprocess: bool, download_dir=None, paper_id=None):
    
    url = "https://arxiv.org/e-print/"
    url = url + paper_id

    headers = {
        "Referer": url,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)\
            Version/16.1 Safari/605.1.15',
        'Accept-Encoding': '*/*',
    }
    
    # try to download Tex files
    try:
        response = requests.head(url, headers=headers, allow_redirects=True)
        response = requests.get(url,  headers=headers)

        filename = '_' + paper_id + '_'
        file_path = os.path.join(download_dir, filename)
        if os.path.exists(file_path):
            return 
        urllib.request.urlretrieve(url, file_path)
    except Exception as e:
        logging.error(f'fails to download {paper_id} tex because of {e}')
    
    if not isprocess:
        # Random Sleep    
        time.sleep(random.randint(30, 40))
    
    return file_path

# download Tex file and process Tex file
def download_and_process(download_dir: str, temp_dir: str, target_dir:str, paper_id=None):
    tex_path = download_tex(True, download_dir, paper_id)
    process_data(temp_dir, target_dir, tex_path)
    
    return 
    

# Process data according to the provided tex file path
def process_data(temp_dir: str, target_dir:str, tex_path: str):
    """
    Processes a TeX file by unzipping, compiling to PDF, generating HTML and JSON, and moving the results to the target directory.
    :param temp_dir: Temporary directory for processing files.
    :param target_dir: Target directory where processed files will be stored.
    :param tex_path: Path to the TeX file to process.
    :return: True if processing is successful, False otherwise.
    """
    # Get the Tex files
    identity = os.path.basename(tex_path)
    # Check to see if thr tex file has been processed
    target_pdf = os.path.join(target_dir, 'pdf')
    target_html = os.path.join(target_dir, 'html')
    target_json = os.path.join(target_dir, 'json')
    for subdir in [target_pdf, target_html, target_json]:
        os.makedirs(subdir, exist_ok=True)
    
    with tempfile.TemporaryDirectory(dir=temp_dir) as temp_dir_id:
        if not unzip_Tex_file(tex_path, temp_dir_id):
            return False
        if not generate_pdf(temp_dir_id, identity):
            return False
        if not generate_html(temp_dir_id, identity):
            return False
        
        pdf_path = os.path.join(temp_dir_id, 'pdf')
        pdf_path = os.path.join(pdf_path, identity + '.pdf')
        if not generate_json(temp_dir_id, pdf_path, identity):
            return False

        temp_pdf = os.path.join(temp_dir_id, 'pdf')
        temp_json = os.path.join(temp_dir_id, 'json')
        temp_html = os.path.join(temp_dir_id, 'html')
        # Move files to their respective target directories
        shutil.move(os.path.join(temp_pdf, f'{identity}.pdf'), target_pdf)
        shutil.move(os.path.join(temp_json, f'{identity}.json'), target_json)
        shutil.move(os.path.join(temp_html, f'{identity}.html'), target_html)
        
        return True


    
# Extract the Tex file to the specified directory
def unzip_Tex_file(tex_path:str, temp_dir:str):    
    temp_dir = os.path.join(temp_dir, 'tex')
    os.makedirs(temp_dir, exist_ok=True)
    tar_file = True
    
    # Use MiME types to check the true type of the file
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(tex_path)
    try:
        # Select a decompression method based on the file type
        if 'zip' in file_type and 'gzip' not in file_type:
            with zipfile.ZipFile(tex_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
        elif 'x-tar' in file_type or 'gzip' in file_type:
            with tarfile.open(tex_path, 'r:*') as tar_ref:
                tar_ref.extractall(temp_dir)
        elif 'x-rar' in file_type:
            with rarfile.RarFile(tex_path, 'r') as rar_ref:
                rar_ref.extractall(temp_dir)
    except Exception as e:
        logging.error(f'{os.path.basename(tex_path)} fails to be depressed, because {e}')
    
    # Check whether the file is successfully decompressed    
    if not os.listdir(temp_dir):
        tar_file = False

    return temp_dir, tar_file

# Use Tex file to compile PDF file
def generate_pdf(temp_dir:str, identity: str):
    # Tex folder
    tex_folder = os.path.join(temp_dir, 'tex')
    # Create a temporary folder for storing PDFS
    temp_pdf = os.path.join(temp_dir, 'pdf')
    os.makedirs(temp_pdf,exist_ok=True)
    
    # Try compiling the PDF file 3 times
    compile_pdf = False
    for i in range(3):
        latexmk = subprocess.Popen(['latexmk','-pdf','-quiet','-interaction=nonstopmode',f'-outdir={temp_pdf}'],cwd=tex_folder,
                                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        try:
            exit_code = latexmk.wait(timeout=60)
        except subprocess.TimeoutExpired as e:
            latexmk.kill()
        # Check whether the PDF is compiled
        pdf_files = [file for file in os.listdir(temp_pdf) if file.endswith('.pdf')]
        if len(pdf_files) != 0:
            compile_pdf = True
            break
    
    if not compile_pdf:
        logging.info(f'{identity} has failed to be compiled to PDF')
        return False
    
    # Rename PDF
    pdf_path = os.path.join(temp_pdf,pdf_files[0])
    target_pdf = os.path.join(temp_pdf, f'{identity}.pdf')
    os.rename(pdf_path, target_pdf)
    
    return True

# Compile Tex to HTML5
def generate_html(temp_dir:str, identity: str):
    # Create a temporary folder for storing html
    temp_html = os.path.join(temp_dir, 'html')
    os.makedirs(temp_html,exist_ok=True)

    html_name = identity + '.html'        
    html_path = os.path.join(temp_html,html_name)

    # Find the main tex
    temp_tex = os.path.join(temp_dir, 'tex')
    files = os.listdir(temp_tex)
    main_tex = ''
    tex_size = 0
    for file_path in files:
        # 合成文件路径
        file_path = os.path.join(temp_tex, file_path)
        if file_path.endswith('.tex'):
            # 判断文件大小
            if os.path.getsize(file_path) > tex_size:
                main_tex = file_path
                tex_size = os.path.getsize(file_path)
    if not main_tex:
        return False
    
    # Try compile html file 2 times
    compile_html = False
    for i in range(2):
        latexmlc = subprocess.Popen(['latexmlc', main_tex, f'--dest={html_path}','--quiet'],cwd=temp_html,
                                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        try:
            exist_code = latexmlc.wait(timeout=90)
        except subprocess.TimeoutExpired as e:
            latexmlc.kill()
        if os.path.exists(html_path):
           compile_html = True 
           break
       
    return compile_html

# Extract diagrams, tables from PDF to json file
def generate_json(temp_dir:str, pdf_path: str, identity: str):
    # Create a temporary folder for storing PDFS
    temp_json = os.path.join(temp_dir, 'json')
    os.makedirs(temp_json,exist_ok=True)    
    json_path = os.path.join(temp_json, identity + '.json')
    
    # Try compiling json file 3 times
    compile_json = False
    for i in range(3):
        pdffigure = subprocess.Popen(
            ["java", "-jar",PDFFIGURES2_JAR_PATH,
            "-d", f"{temp_json}/","-c", "-q", pdf_path],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
            )
        try:
            exit_code = pdffigure.wait(timeout=60)
        except subprocess.TimeoutExpired as e:
            pdffigure.kill()
        if os.path.exists(json_path):
            compile_json = True  
            break
    
    return compile_json
    
# Use multiple processes to process data
def process(args): 
    # Create output folder
    output_dir = os.path.realpath(args.output_dir)
    temp_dir = os.path.join(output_dir, 'temp')
    target_dir = os.path.join(output_dir, 'arxiv')
    for subdir in [output_dir,temp_dir, target_dir]:
        os.makedirs(subdir, exist_ok=True)

    # Create log
    log_path = os.path.join(output_dir, 'process.log')
    create_log(log_path)

    # Check the environment variable for pdffigures2
    global PDFFIGURES2_JAR_PATH
    
    PDFFIGURES2_JAR_PATH = os.environ.get("PDFFIGURES_PATH", None)
    if not PDFFIGURES2_JAR_PATH:
        logging.info("please set environment variables -- PDFFIGURES_JAR_PATH")
        return 

    if args.data_path:
        data_path = os.path.realpath(args.data_path)
        tex_files = tqdm([os.path.join(data_path, file) for file in os.listdir(data_path)])
    else:
        logging.error('Please provide path of folder that contains Tex files')
    
    # Use multiple processes to process data
    process_func = partial(process_data, temp_dir, target_dir)
    results = process_map(process_func, tex_files, max_workers=args.num_workers, chunksize=1)
    
    logging.info('Process Job has finished!')
    
    return
        
# Use multiple processes to crawl paper
def crawl(args):
    # Parse parameters
    start_page = args.start_page
    end_page = args.end_page
    num_workers = args.num_workers
    year = args.year
    identity = args.identity
    per_page = args.per_page
    output_dir = args.output_dir
    
    # Create output folder
    os.makedirs(output_dir, exist_ok=True)
    
    # Create log file
    log_path = os.path.join(output_dir, 'crawl.log')
    create_log(log_path)
    logging.info('job has begun')

    pages = tqdm([page for page in range(start_page, end_page + 1)])
    doi_path = os.path.join(output_dir, 'link.txt')
    
    # Create a process pool to get link information
    pool = multiprocessing.Pool(processes=num_workers)
    process_func = partial(crawl_arxiv, identity, year, per_page, doi_path)
    results_links = pool.map(process_func, pages)
    pool.close()
    pool.join()
    
    doi_list = []
    # Record the link information
    with open(doi_path, 'w') as f:
        for links in results_links:
            doi_list.extend(links)
            f.write('\n'.join(links))        
    doi_list = tqdm(doi_list)
    logging.info(f'the length of doi_list is {len(doi_list)}')
    
    # Create a process pool to download Tex files
    download_dir = os.path.join(output_dir, 'tex')
    
    process_func = partial(download_tex, False, download_dir)
    results = process_map(process_func, doi_list, max_workers=num_workers, chunksize=1)
    logging.info('job has finished')

    return


def crawl_and_process(args):
    # Create output folder
    output_dir = os.path.realpath(args.output_dir)
    start_page = args.start_page
    end_page = args.end_page
    num_workers = args.num_workers
    year = args.year
    identity = args.identity
    per_page = args.per_page
    
    # Create Related Output Folder
    temp_dir = os.path.join(output_dir, 'temp')
    target_dir = os.path.join(output_dir, 'arxiv')
    download_dir = os.path.join(output_dir, f'{identity}')
    
    for subdir in [output_dir, temp_dir, target_dir, download_dir]:
        os.makedirs(subdir,exist_ok=True)
    
    # Create log file
    log_path = os.path.join(output_dir, 'crawl.log')
    create_log(log_path)
    logging.info('job has begun')
    
    # Check the environment variable for pdffigures2
    global PDFFIGURES2_JAR_PATH
    
    PDFFIGURES2_JAR_PATH = os.environ.get("PDFFIGURES_PATH", None)
    if not PDFFIGURES2_JAR_PATH:
        logging.info("please set environment variables -- PDFFIGURES_JAR_PATH")
        return 
    
    pages = tqdm([page for page in range(start_page, end_page + 1)])
    doi_path = os.path.join(output_dir, 'link.txt')
    
    # Create a process pool to get link information
    pool = multiprocessing.Pool(processes=num_workers)
    process_func = partial(crawl_arxiv, identity, year, per_page)
    results_links = pool.map(process_func, pages)
    pool.close()
    pool.join()
    
    # Record the link information
    doi_list = []
    with open(doi_path, 'w') as f:
        for links in results_links:
            doi_list.extend(links)
            f.write('\n'.join(links))        
    doi_list = tqdm(doi_list)
    logging.info(f'the length of doi_list is {len(doi_list)}')
    
    # Create a process pool to get link information
    results = process_map(partial(download_and_process, download_dir, temp_dir, target_dir),
                        doi_list, max_workers=num_workers, chunksize=1)
    return 

    
    