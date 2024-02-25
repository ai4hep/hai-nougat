import hai
from pathlib import Path
import hai_model, os, time
import PyPDF2, logging
import math
import gradio as gr
import tempfile
import threading,re

# 这个函数将在后台运行，在一定延迟后删除文件
def delete_file_later(file_path, delay=300):
    time.sleep(delay)  # 等待指定的延迟时间（秒）
    if os.path.exists(file_path):
        os.remove(file_path)  # 删除文件

# 这是处理上传文件的函数
def process_file(uploaded_file):
    # 发起API请求，传递文件的字节数据
    ret = hai_model.HaiModel.inference(
        model= r'meta/nougat',
        timeout=300,
        stream=False,
        pdf_path=uploaded_file.name,
        url= "http://aiapi.ihep.ac.cn:42901",
        api_key="Hi-fxpWxALpzzeAFLhYyQLcDEoBRDyhEneGrnJlPDDUPIPcKBP"
    )
    with tempfile.NamedTemporaryFile(delete=False,  suffix='.mmd') as tmp_file:
        # 将上传的文件内容写入临时文件
        tmp_file.write(ret.encode('utf-8'))
        tmp_file_path = tmp_file.name  # 获取临时文件的路径作为字符串
    
    # 启动一个后台线程，在延迟后删除文件
    threading.Thread(target=delete_file_later, args=(tmp_file_path,)).start()

    return tmp_file_path

# 创建 Gradio 界面
iface = gr.Interface(
    fn=process_file,  # 设置处理函数
    inputs=gr.File(label="Upload PDF", type='filepath', file_types=[".pdf"]),  # 设置输入为文件上传
    outputs=gr.File(label="Download Output", type='filepath'),  # 设置输出为文件下载
    title="HaiNougat",  # 界面标题
    description="Upload a pdf and download Output that HaiNougat generates. You can use the Mathpix Markdown extension on Vscode to render and view the file."  # 界面描述
)

# 启动界面
iface.launch(share=True, server_name='0.0.0.0', server_port=7860, quiet=True)

