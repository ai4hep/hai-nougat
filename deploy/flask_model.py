from flask import Flask, request, jsonify, abort
from flask_cors import CORS  # 导入 CORS
import hai_model
import tempfile, threading, os
from gevent import pywsgi
from werkzeug.utils import secure_filename
import magic
from PyPDF2 import PdfReader
import PyPDF2

app = Flask(__name__)
CORS(app) 
api_key = os.environ.get("HEPAI_API_KEY", None)
# 设置最大并发数量
semaphore = threading.Semaphore(20)

def is_valid_pdf(file_stream):
    try:
        PdfReader(file_stream)
        return True
    except (PyPDF2.errors.PdfReadError, AssertionError):
        return False

def get_mime_type(file_path):
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)
    
# 这是处理上传文件的函数
def process_file(uploaded_file_path):

    # 发起API请求，传递文件的字节数据
    ret = hai_model.HaiModel.inference(
        model='meta/nougat',
        timeout=3000,
        stream=False,
        pdf_path=uploaded_file_path,
        url="http://aiapi.ihep.ac.cn:42901",
        api_key=api_key
    )

    return ret

@app.route('/upload', methods=['POST'])
def upload_file():
    if not semaphore.acquire(blocking=False):
        # 信号量无法获取，返回429状态码
        return jsonify({'error': 'Too many requests'}), 429
    try:
        if 'file' not in request.files:
            return abort(400, 'No file part')
        file = request.files['file']
        if file.filename == '':
            return abort(400, 'No selected file')
        
        if not is_valid_pdf(file.stream):
            return abort(400, 'File is not a PDF')
        file.stream.seek(0)  # 重置文件流的位置
    
        # 为了安全起见，使用 secure_filename 函数获取安全的文件名
        original_filename = secure_filename(file.filename)
        with tempfile.NamedTemporaryFile(prefix=original_filename + "_", suffix='.pdf', delete=True) as temp_pdf:
            file.save(temp_pdf.name)
            # 假设 temp_pdf 是临时保存的 PDF 文件的路径
            mime_type = get_mime_type(temp_pdf.name)
            if mime_type != 'application/pdf':
                return abort(400, 'File is not a PDF')
            try:
                # 假设 process_file 函数返回处理后的数据字符串
                processed_data = process_file(temp_pdf.name)
            except Exception as e:
                app.logger.error(f"File processing failed: {e}")
                return abort(500, 'File processing failed')
    finally:
        semaphore.release()

    # 直接返回处理后的数据给前端
    return jsonify({
        'message': 'File processed successfully',
        'content': processed_data
    }), 201

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 7880), app)
    server.serve_forever()