import hai
from pathlib import Path
import hai_model

hai.api_key = ""

# 发起API请求，传递文件的字节数据
ret = hai_model.HaiModel.inference(
    model= r'meta/nougat',
    timeout=90,
    stream=True,
    url= "http://aiapi.ihep.ac.cn:42901",
    pdf_path = "../nougat.pdf",
)

save_path = Path('../test.md')
save_path.write_text(ret, encoding="utf-8")
