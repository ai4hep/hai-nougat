import requests
import os
import hai,base64
import pypdfium2
from pathlib import Path

with open('/home/luojw/VSProjects/hai-nougat/test.pdf', 'rb') as pdf_file:
    pdfbin = pdf_file.read()

# 将字节数据编码为 Base64 字符串
pdfbin= base64.b64encode(pdfbin).decode()


data = {'pdfbin': pdfbin}

session = requests.Session()
response = session.post(
    # response = requests.post(
    'http://127.0.0.1:42905/worker_generate_stream',
    json=data,
    timeout=600,
    stream=True
)

data= response.json()
print(response.text)

save_path = Path('/home/luojw/VSProjects/hai-nougat/test.mmd')
save_path.write_text(response.text, encoding="utf-8")
