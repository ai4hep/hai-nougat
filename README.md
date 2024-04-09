[![Stars](https://img.shields.io/github/stars/ai4hep/hai-nougat)](
https://github.com/zhangzhengde0225/Xiwu)

# <img width="8%" src='/web/build/static/media/logo.86df30241577a42b7e0f.png' alt="logo"> HaiNougat


This project is the official implemention of **HaiNougat: A More Accurate Document Parser for High-Energy Physics**, which if an academic document PDF parser specialized in converting high-energy physics documents into Mathpix Markdown format.

You can access the HaiNougat WebUI [here](https://ai.ihep.ac.cn/m/hai-nougat).

## Data-Clean Tool

This tool is capable of crawling specified domains and years of documents from [ArXiv](https://arxiv.org/), and automatically processing them into an AI-ready dataset.

### Install

First `cd data-clean-tool`

Next run `pip install -r requirements`

Then, Download [TeX Live 2023](https://tug.org/texlive/), [LaTeXML](https://github.com/brucemiller/LaTeXML), [pdffigures2](https://github.com/allenai/pdffigures2), and set them as environment variables.

### Usage

First `cd data-clean-tool`

Next run

`python main.py --crawl --start-page 0 --end-page 10 --year 23 --identity hep-ex --per-page 500 --process --output-folder /path/output --num-workers 8 `  to collect and process data.

Here are  descriptions of the parameters:

| Argument        | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| `--crawl`       | Crawl papers                                                 |
| `--start-page`  | The start page you want to crawl                             |
| `--end-page`    | The end page you want to crawl                               |
| `--per-page`    | The number of papers that one page stores                    |
| `--identity`    | The id of the subject, like hep-ex,hep-lat                   |
| `--year`        | the year of the paper that you want to crawl                 |
| `--process`     | Process files                                                |
| `--data-path`   | File that contains Tex files, if you set `--crawl`,  then the parameters can be ignored. |
| `--output-dir`  | The folder that stores output                                |
| `--num-workers` | The number of processes for data processing                  |

Then, you will get 3 folders:

1. A directory containing the PDFs
2. A directory containing the `.html` files (processed `.tex` files by [LaTeXML](https://math.nist.gov/~BMiller/LaTeXML/)) with the same folder structure
3. A binary file of [pdffigures2](https://github.com/allenai/pdffigures2) and a corresponding environment variable `export PDFFIGURES_PATH="/path/to/binary.jar"`

### Generate Dataset

### Next run

```python
python -m nougat.dataset.split_htmls_to_pages --html path/html/root --pdfs path/pdf/root --out path/paired/output --figure path/pdffigures/outputs
```

Additional arguments include

| Argument              | Description                                |
| --------------------- | ------------------------------------------ |
| `--recompute`         | recompute all splits                       |
| `--markdown MARKDOWN` | Markdown output dir                        |
| `--workers WORKERS`   | How many processes to use                  |
| `--dpi DPI`           | What resolution the pages will be saved at |
| `--timeout TIMEOUT`   | max time per paper in seconds              |
| `--tesseract`         | Tesseract OCR prediction for each page     |

Finally create a `jsonl` file that contains all the image paths, markdown text and meta information.

```
python -m nougat.dataset.create_index --dir path/paired/output --out index.jsonl
```

For each `jsonl` file you also need to generate a seek map for faster data loading:

```
python -m nougat.dataset.gen_seek file.jsonl
```

The resulting directory structure can look as follows:

```
root/
├── images
├── train.jsonl
├── train.seek.map
├── test.jsonl
├── test.seek.map
├── validation.jsonl
└── validation.seek.map
```

## WebUI

### Install

```
cd web
pip install -r requirements.txt
```

### Usage

First, you need to add your API key to the environment variable `HEPAI_API_KEY`

Then, run `python app.py`. This webpage will start on the port `7860`.

You can also visit the [WebUI](https://ai.ihep.ac.cn/m/hai-nougat) to experience the HaiNougat model.

## Worker

This guide demonstrates how to deploy HaiNougat as a worker and enable requests using an API key. 

## Install

```
cd worker

pip install -r requirments.txt
```

## Usage

First, `cd deploy`

Then, Set the environment variable `HEPAI_API_KEY` to your API key 

Next, run `chmod +x ./run_worker.sh`

Finally, run `./run_worker.sh`

To deploy the worker to a different address, you can replace the `http://aiapi.ihep.ac.cn:42901`  in the `run_worker.sh` with the desired address and port in the command. 

## Citation

```
@misc{Luo2024hainougat,
      title={HaiNougat: A More Accurate Document Parser for High-Energy Physics}, 
      author={Jianwen Luo, Zhengde Zhang*, Fazhi Qi, Yiyu Zhang},
      year={2024}
      url={https://github.con/ai4hep/hai-nougat}
}
```

## Acknowledgements

The creation of this work owes a great deal to the incredible open source models and datasets that have been utilized, among which include (but are not limited to):

* Nougat from Meta


## License

HaiNougat is licensed under CC-BY-NC.

If used for commercial purposes, please contact `zdzhang@ihep.ac.cn`.
