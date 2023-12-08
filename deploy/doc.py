import requests,base64

with open('/home/luojw/VSProjects/hai-nougat/test.pdf', 'rb') as pdf_file:
    pdfbin = pdf_file.read()


# 将字节数据编码为 Base64 字符串
pdfbin= base64.b64encode(pdfbin).decode()

response = requests.post(
        "http://192.168.60.170:42901/v1/inference",
        json={
            "model": "meta/nougat-test",
            "stream": False,
            "stream_interval": 0.0,
            "only_num_tokens": True,
            "pdfbin": pdfbin
        },
        stream=False,
    )

print(response.text)