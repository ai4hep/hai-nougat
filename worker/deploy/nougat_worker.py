import hai,os
from hai import BaseWorkerModel
from dataclasses import dataclass
import sys, logging,base64,torch
from pathlib import Path
import pypdfium2
here = Path(__file__).parent.absolute()
sys.path.append(f'{here.parent}')
from apis import partial
from apis import move_to_device, get_checkpoint,ImageDataset
from nougat_model import NougatModel
from nougat_inference import inference_no_stream, inference_stream
from utils import rasterize_paper

class WorkerModel(BaseWorkerModel):
    def __init__(self, name, **kwargs):
        self.name = name 
        self.checkpoint = str(here.parent / 'checkpoint')
        self.batchsize = self.determine_batchsize()
        self.nougat_model = self.initialize_model()
        

    def determine_batchsize(self):
        if torch.cuda.is_available():
            batchszie = int(
                torch.cuda.get_device_properties(0).total_memory / 1024 / 1024 / 1000 * 0.3
            )
            if batchszie == 0:
                logging.warning("GPU VRAM is too small. Computing on CPU.")
        elif torch.backends.mps.is_available():
            batchszie = 4
        else:
            batchszie = 1
            logging.warning("No GPU found. Conversion on CPU is very slow.")
        return batchszie
    
    def initialize_model(self):
        model = NougatModel.from_pretrained(get_checkpoint(checkpoint_path=self.checkpoint))
        model = move_to_device(model, cuda=self.batchsize > 0)
        if self.batchsize <= 0:
            self.batchsize = 1
        model.eval()
        return model
        
    def inference(self, **kwargs):
        pdfbin = kwargs.pop('pdfbin')
        start = kwargs.pop('start', None)
        stop = kwargs.pop('stop', None)
        stream = kwargs.get('stream', False)
        pdfbin = base64.b64decode(pdfbin)
        pdf = pypdfium2.PdfDocument(pdfbin)
        if start is not None and stop is not None:
            pages = list(range(start - 1, stop))
        else:
            pages = list(range(len(pdf)))        
        compute_pages = pages.copy()
        
        images = rasterize_paper(pdf, pages=compute_pages)
        dataset = ImageDataset(
            images,
            partial(self.nougat_model.encoder.prepare_input, random_padding=False),
        )
        dataloader = torch.utils.data.DataLoader(
            dataset,
            batch_size=self.batchsize,
            pin_memory=True,
            shuffle=False
        )
        if stream:
            return inference_stream(dataloader=dataloader, nougat_model=self.nougat_model, pages=pages, compute_pages=compute_pages, batch=self.batchsize)
        else:
            return inference_no_stream(dataloader=dataloader, nougat_model=self.nougat_model, pages=pages, compute_pages=compute_pages, batch=self.batchsize)

    

def run_worker(**kwargs):
    model_args, worker_args = hai.parse_args_into_dataclasses((ModelArgs, WorkerArgs))  # 解析多个参数类

    model = WorkerModel(  # 获取模型
        name=model_args.name
        )
    if worker_args.test:
        pdf_path = ""
        pdf_path = os.path.abspath(pdf_path)
        if not os.path.exists(pdf_path):
            raise ValueError("PDF路径为空.请使用pdlf_path参数来提供有效的PDF路径。")
        else:
            with open(pdf_path, 'rb') as pdf_file:
                pdfbin = pdf_file.read()          
        pdfbin= base64.b64encode(pdfbin).decode()
    
        ret = model.inference(pdfbin=pdfbin, stream=False)
        print(ret)
        return

    hai.worker.start(
        model=model,
        worker_args=worker_args,
        **kwargs 
        )

@dataclass
class ModelArgs:
    name: str = "hepai/hainougat"  # worker的名称，用于注册到控制器


# (2) worker的参数配置和启动代码
@dataclass
class WorkerArgs:
    host: str = "0.0.0.0"  # worker的地址，0.0.0.0表示外部可访问，127.0.0.1表示只有本机可访问
    port: str = "auto"  # worker的端口，默认从42902开始自动分配
    controller_address: str = "https://aiapi.ihep.ac.cn"  # 控制器的地址
    worker_address: str = "auto"  # 默认是http://<ip>:<port>
    limit_model_concurrency: int = 5  # 限制模型的并发请求
    stream_interval: float = 0.  # 额外的流式响应间隔
    no_register: bool = False  # 不注册到控制器
    permissions: str = 'groups: payg ; owner: tangzh@ihep.ac.cn'  # 模型的权限授予，分为用户和组，用;分隔，例如：需要授权给所有组、a用户、b用户：'groups: all; users: a, b; owner: c'
    description: str = 'This is a demo worker in HepAI-Distributed Deploy Framework'  # 模型的描述
    author: str = 'admin'  # 模型的作者
    test: bool = False  # 测试模式，不会真正启动worker，只会打印参数

if __name__ == '__main__':
    run_worker()
