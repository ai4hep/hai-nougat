import hai, logging
from hai import BaseWorkerModel
from dataclasses import dataclass, field
import os, sys, logging,base64,time
from pathlib import Path
here = Path(__file__).parent.absolute()
sys.path.append(f'{here.parent.parent}')
from HaiNougat.apis import train
from HaiNougat.apis import partial
from HaiNougat.apis import hashlib
from HaiNougat.apis import pypdfium2
from HaiNougat.apis import torch
from nougat_model import NougatModel
from HaiNougat.apis import markdown_compatible, close_envs
from HaiNougat.apis import ImageDataset
from HaiNougat.apis import get_checkpoint
from HaiNougat.apis import rasterize_paper
from HaiNougat.apis import move_to_device, default_batch_size
from HaiNougat.apis import tqdm
import torch
import torch.nn as nn
import torch.distributed as dist
from functools import partial
import pypdfium2
import torch.multiprocessing as mp

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
    logging.getLogger('').addHandler(streamlog)
    return


class WorkerModel(BaseWorkerModel):
    def __init__(self, name, **kwargs):
        self.name = name 
        self.model = self.initialize_model()
        self.batchsize = self.determine_batchsize()
        self.device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
        

    def determine_batchsize(self):
        if torch.cuda.is_available():
            batchszie = int(
                torch.cuda.get_device_properties(0).total_memory / 1024 / 1024 / 1000 * 0.3
            )
            if batchszie == 0:
                logging.warning("GPU VRAM is too small. Computing on CPU.")
        elif torch.backends.mps.is_available():
            # I don't know if there's an equivalent API so heuristically choosing bs=4
            batchszie = 4
        else:
            # don't know what a good value is here. Would not recommend to run on CPU
            batchszie = 1
            logging.warning("No GPU found. Conversion on CPU is very slow.")
        return batchszie
    
    def initialize_model(self):
        model = NougatModel.from_pretrained(get_checkpoint())
        try:
            if torch.backends.mps.is_available():
                return model.to("mps")
        except AttributeError:
            pass
        model = model.to(torch.bfloat16)
        model.to("cuda:1")
        model.eval()
        return model


    def inference(self, **kwargs):
        # 自己的执行逻辑, 例如: # 
    
        pdfbin = kwargs.pop('pdfbin')
        start = kwargs.pop('start', None)
        stop = kwargs.pop('stop', None)
        
        pdfbin = base64.b64decode(pdfbin)
        
        pdf = pypdfium2.PdfDocument(pdfbin)
    
        if start is not None and stop is not None:
            pages = list(range(start - 1, stop))
        else:
            pages = list(range(len(pdf)))
        
        compute_pages = pages.copy()
        predictions = [""] * len(pages)

        images = rasterize_paper(pdf, pages=compute_pages)
        
        dataset = ImageDataset(
            images,
            partial(self.model.encoder.prepare_input, random_padding=False),
        )

        dataloader = torch.utils.data.DataLoader(
            dataset,
            batch_size=self.batchsize,
            pin_memory=True,
            shuffle=False,
        )

        for idx, sample in tqdm(enumerate(dataloader), total=len(dataloader)):
            if sample is None:
                continue
            model_output = self.model.inference(image_tensors=sample)
            for j, output in enumerate(model_output["predictions"]):
                if model_output["repeats"][j] is not None:
                    if model_output["repeats"][j] > 0:
                        disclaimer = "\n\n+++ ==WARNING: Truncated because of repetitions==\n%s\n+++\n\n"
                    else:
                        disclaimer = (
                            "\n\n+++ ==ERROR: No output for this page==\n%s\n+++\n\n"
                        )
                    rest = close_envs(model_output["repetitions"][j]).strip()
                    if len(rest) > 0:
                        disclaimer = disclaimer % rest
                    else:
                        disclaimer = ""
                else:
                    disclaimer = ""
                
                predictions[pages.index(compute_pages[idx * self.batchsize + j])] = (
                    markdown_compatible(output) + disclaimer
                )
                print(pages.index(compute_pages[idx * self.batchsize + j]))
            print('\n\n')
        
        time1 = time.time()
        final = "".join(predictions).strip()
        time2 = time.time()
        print(round(time2-time1,2))

        return final


if __name__ == "__main__":
    with open('/home/luojw/VSProjects/hai-nougat/test.pdf', 'rb') as pdf_file:
        pdfbin = pdf_file.read()

    create_log('/home/luojw/VSProjects/hai-nougat/output.log')

    # 将字节数据编码为 Base64 字符串
    pdfbin= base64.b64encode(pdfbin).decode()

    # 设置API密钥
    hai.api_key = os.getenv("HEPAI_API_KEY")

    ret = WorkerModel(name=1).inference(pdfbin=pdfbin)

    save_path = Path('/home/luojw/VSProjects/hai-nougat/test.mmd')
    save_path.write_text(ret, encoding="utf-8")