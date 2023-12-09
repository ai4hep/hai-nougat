import hai
from hai import BaseWorkerModel
from dataclasses import dataclass, field
import os, sys
from pathlib import Path
here = Path(__file__).parent.absolute()

try:
    from HaiNougat.apis import train
except:
    sys.path.append(f'{here.parent.parent}')
    from HaiNougat.apis import train

# from HaiNougat.apis i

class WorkerModel(BaseWorkerModel):
    def __init__(self, name, **kwargs):
        self.name = name  # name属性用于用于请求指定调研的模型

    @BaseWorkerModel.auto_stream  # 自动将各种类型的输出转为流式输
    def inference(self, **kwargs):
        # 自己的执行逻辑, 例如: # 
        file = kwargs.pop('file')
        start = kwargs.pop('start', None)
        end = kwargs.pop('stop', None)
        
        # 处理逻辑
        input = kwargs.pop('input', None)
        output = [1, 2, 3, 4, 5]  # 修改为自己的输出
        return output, input

def run_worker(**kwargs):
    # worker_args = hai.parse_args_into_dataclasses(WorkerArgs)  # 解析参数
    model_args, worker_args = hai.parse_args_into_dataclasses((ModelArgs, WorkerArgs))  # 解析多个参数类
    # print(worker_args)
    model = WorkerModel(  # 获取模型
        name=model_args.name
        # 此处可以传入其他参数
        )
    
    if worker_args.test:
        ret = model.inference(input='test')
        print(ret)
        return

    hai.worker.start(
        model=model,
        worker_args=worker_args,
        **kwargs
        )

# (1) 实现WorkerModel
@dataclass
class ModelArgs:
    name: str = "meta/nougat"  # worker的名称，用于注册到控制器
    # 其他参数

# (2) worker的参数配置和启动代码
@dataclass
class WorkerArgs:
    host: str = "0.0.0.0"  # worker的地址，0.0.0.0表示外部可访问，127.0.0.1表示只有本机可访问
    port: str = "auto"  # worker的端口，默认从42902开始自动分配
    controller_address: str = "http://aiapi.ihep.ac.cn:42901"  # 控制器的地址
    worker_address: str = "auto"  # 默认是http://<ip>:<port>
    limit_model_concurrency: int = 5  # 限制模型的并发请求
    stream_interval: float = 0.  # 额外的流式响应间隔
    no_register: bool = False  # 不注册到控制器
    permissions: str = 'groups: all'  # 模型的权限授予，分为用户和组，用;分隔，例如：需要授权给所有组、a用户、b用户：'groups: all; users: a, b; owner: c'
    description: str = 'This is a demo worker in HeiAI-Distributed Deploy Framework'  # 模型的描述
    author: str = 'meta'  # 模型的作者
    test: bool = False  # 测试模式，不会真正启动worker，只会打印参数

if __name__ == '__main__':
    run_worker()