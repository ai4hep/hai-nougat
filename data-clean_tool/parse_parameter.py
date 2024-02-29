import argparse


def parse_arg(args):
    parser = argparse.ArgumentParser(description='Generate Data')
    
    # Crawl papers from Arxiv
    parser.add_argument('--crawl', action='store_true', help='Crawl papers')
    parser.add_argument('--start-page', type=int, default=0, dest='start_page',
                        help="the start page you want to crawl")
    parser.add_argument('--end-page', type=int, default=40, dest='end_page',
                        help="the end page you want to crawl")
    parser.add_argument('--per-page', type=int, default=500, dest="per_page",
                        help="One page stores the number of papers")
    parser.add_argument('--identity',type=str, default='hep-ex', dest='identity',
                        help="The id of the subject, like cs.AI" )
    parser.add_argument('--year', type=int, default=23, dest="year",
                        help="the year of the paper")
  
    # Process Tex Files
    parser.add_argument('--process', action='store_true', help='Process files')
    parser.add_argument('--data-path', dest='data_path',
                        type=str,
                        help=('file that contains Tex files'
                        ))
    
    
    parser.add_argument('--output-dir', type=str, default='', dest="output_dir",
                        help="the folder that stores output")
    parser.add_argument('--num-workers',default=8,type=int, dest="num_workers",
                        help=("num workers to process data"))
    
    parameters = parser.parse_args(args)
    return parameters
