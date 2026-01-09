from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
import tempfile
import traceback, asyncio, os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from werkzeug.utils import secure_filename
from utils import ConcurrencyLimiter, is_valid_pdf, process_file

app = FastAPI()
app.mount("/static", StaticFiles(directory="build/static"), name="static")
templates = Jinja2Templates(directory="build")

# 设置最大并发数
MAX_CONCURRENT_REQUESTS = 5
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.environ.get("HEPAI_API_KEY", None)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    async with ConcurrencyLimiter(semaphore):
        if not file.content_type == 'application/pdf':
            raise HTTPException(status_code=400, detail="File is not a PDF")
        if not is_valid_pdf(file.file):
            raise HTTPException(status_code=400, detail="File is not a PDF")
        file.file.seek(0)
        try:
            original_filename = secure_filename(file.filename)
            with tempfile.NamedTemporaryFile(prefix=original_filename + "_", suffix='.pdf', delete=True) as temp_pdf:
                content = await file.read()
                # 将内容写入临时文件
                temp_pdf.write(content)
                # 必须调用 flush() 来确保所有内容都被写入磁盘
                temp_pdf.flush()  
                processed_data = await process_file(temp_pdf.name, api_key)    
        except Exception as e:
            traceback.print_exc()  # 打印异常堆栈信息到控制台
            raise HTTPException(status_code=500, detail=str(e))
        
        return {
            'message': 'File processed successfully',
            'content': processed_data
        }
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)