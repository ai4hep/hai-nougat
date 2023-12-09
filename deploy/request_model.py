import hai
from pathlib import Path
import hai_model


# 发起API请求，传递文件的字节数据
ret = hai_model.HaiModel.inference(
    model= r'meta/nougat',
    timeout=90,
    stream=False,
    url= "http://aiapi.ihep.ac.cn:42901",
    pdf_path = "/home/luojw/VSProjects/hai-nougat/HaiNougat/nougat.pdf",
    api_key="Hi-VTAYsGaZmTIouTCOfSBeThEHyEuLfGhrpRDFODkfFkZkpEu",
    start=10,
    stop=10
)
print(ret)
save_path = Path('/home/luojw/VSProjects/hai-nougat/test.md')
save_path.write_text(ret, encoding="utf-8")
