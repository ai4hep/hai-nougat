import gradio as gr
from pathlib import Path
import fitz
import hai
import hai_model
import numpy as np
import io, os
from PIL import Image
import io

hai.api_key = "Hi-njEDkAlMXvObDsFKbbGOnnPgfLOOeOqlDySIjslzCymXAVZ"
def process_file(upload_file, start_page:None, end_page:None):
    # 读取pdf文本并解析
    try:
        with open(upload_file, "rb") as pdf:
            pdfbin = pdf.read()
            # 使用二进制数据创建 PyMuPDF 文档对象
            pdf_document = fitz.open("pdf", pdfbin)
            # 获取PDF文件的总页数
            total_pages = pdf_document.page_count
    except Exception as e:
        raise ValueError(f"PDF文件解析失败: {e}")
    if not start_page and not end_page:
        if start_page <= 0 or end_page > total_pages:
            raise ValueError("请提供正确的页面范围")
    
    return pdfbin

# 渲染指定页面范围为图片的函数
def pdf_pages_to_images(pdf_path, start_page, end_page, dpi=100):
    pdf = fitz.open(pdf_path)
    images = []
    
    if not start_page and not end_page:
        start_page = 0
        end_page = pdf.page_count - 1
    
    # 验证页面范围
    start_page = max(1, start_page)
    end_page = min(end_page, pdf.page_count - 1)
    
    for page_num in range(start_page - 1, end_page):
        page = pdf[page_num]
        
        # 设置变换矩阵
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data))
        images.append(img)
        yield images

    pdf.close()
   
def generate_result(pdfdata):
    # 发起API请求，传递文件的字节数据
    ret = hai_model.HaiModel.inference(
        model= r'meta/nougat-test',
        timeout=90,
        stream=True,
        url= "http://aiapi.ihep.ac.cn:42901",
        pdfbin = pdfdata
    )
    return ret


# 创建Gradio应用
iface = gr.Interface(
    fn=pdf_pages_to_images,
    inputs=[
        gr.File(),
        gr.Number(label="Start Page"),
        gr.Number(label="End Page")
    ],
    outputs=gr.Gallery(every=0.5)
)

# Rest of your code to launch the interface
iface.queue().launch()

