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


from typing import Dict, Union, Literal
from dataclasses import dataclass, field
import json
import hepai
from hepai import HRModel, HModelConfig, HWorkerConfig, HWorkerAPP

@dataclass  # (1) model config
class CustomModelConfig(HModelConfig):
    name: str = field(default="hepai/hainougat", metadata={"help": "Model's name"})
    version: str = field(default="2.0", metadata={"help": "Model's version"})

@dataclass  # (2) worker config
class CustomWorkerConfig(HWorkerConfig):
    # config for worker server
    host: str = field(default="0.0.0.0", metadata={"help": "Worker's address, enable to access from outside if set to `0.0.0.0`, otherwise only localhost can access"})
    port: int = field(default=42600, metadata={"help": "Worker's port, default is 42600"})
    auto_start_port: int = field(default=42602, metadata={"help": "Worker's start port, only used when port is set to `None`"})
    type: Literal["common", "llm", "actuator", "preceptor", "memory"] = field(default="common", metadata={"help": "Specify worker type, could be help in some cases"})
    speed: int = field(default=1, metadata={"help": "Model's speed"})
    limit_model_concurrency: int = field(default=100, metadata={"help": "Limit the model's concurrency"})
    permissions: str = field(default='users: admin;groups: payg; owner: tangzh@ihep.ac.cn', metadata={"help": "Worker's permissions, separated by ;, e.g., 'groups: default; users: a, b; owner: c'"})
    author: str = field(default=None, metadata={"help": "Model's author"})
    description: str = field(default='This is a custom remote worker created by HepAI.', metadata={"help": "Model's description"})
    
    # config for controller connection
    controller_address: str = field(default="https://aiapi.ihep.ac.cn", metadata={"help": "Controller's address"})
    no_register: bool = field(default=False, metadata={"help": "Do not register to controller"})

# class CustomWorkerModel(HRModel):  # Define a custom worker model inheriting from HRModel.
#     def __init__(self, config: HModelConfig):
#         super().__init__(config=config)

#     @HRModel.remote_callable  # Decorate the function to enable remote call.
#     def custom_method(self, a: int = 1, b: int = 2) -> int:
#         """Define your custom method here."""
#         return a + b
    
#     @HRModel.remote_callable
#     def get_stream(self):
#         for x in range(10):
#             yield f"data: {json.dumps(x)}\n\n"
            


class WorkerModel(HRModel):
    # def __init__(self, name, **kwargs):
    def __init__(self, config: HModelConfig):
        super().__init__(config=config)
        self.name = config.name
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
    
    @HRModel.remote_callable
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
        

if __name__ == "__main__":

    import uvicorn
    from fastapi import FastAPI
    model_config, worker_config = hepai.parse_args((CustomModelConfig, CustomWorkerConfig))
    model = WorkerModel(model_config)  # Instantiate the custom worker model.
    app: FastAPI = HWorkerAPP(models=[model], worker_config=worker_config)  # Instantiate the APP, which is a FastAPI application.
    
    print(app.worker.get_worker_info(), flush=True)
    # 启动服务  
    uvicorn.run(app, host=app.host, port=app.port)