import sys, os
from pathlib import Path
here = Path(__file__).parent.absolute()
sys.path.append(f'{here}')
from apis import hai_model
 
api_key = os.environ.get("HEPAI_API_KEY", None)

# 发起API请求，传递文件的字节数据
ret = hai_model.HaiModel.inference(
    model= r'meta/nougat',
    timeout=300,
    stream=False,
    pdf_path='/path/pdf',
    url= "http://aiapi.ihep.ac.cn:42901",
    api_key=api_key
)

print(ret)
