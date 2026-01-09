from fastapi import HTTPException
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
import hai_model
from PyPDF2 import PdfReader
import PyPDF2, magic, asyncio
from functools import partial

def is_valid_pdf(file_stream):
    try:
        PdfReader(file_stream)
        return True
    except (PyPDF2.errors.PdfReadError, AssertionError):
        return False

def get_mime_type(file_path):
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)

async def process_file(uploaded_file_path, api_key):
    loop = asyncio.get_running_loop()
    inference_func = partial(
        hai_model.HaiModel.inference,
        model='hepai/hainougat',
        timeout=3000,
        stream=False,
        pdf_path=uploaded_file_path,
        url="https://aiapi.ihep.ac.cn",
        api_key=api_key
    )

    # 使用 await 调用 run_in_executor 以在后台线程中执行 inference 函数
    ret = await loop.run_in_executor(None, inference_func)
    return ret

class ConcurrencyLimiter:
    def __init__(self, semaphore: asyncio.Semaphore):
        self.semaphore = semaphore

    async def __aenter__(self):
        if self.semaphore.locked():
            raise HTTPException(
                status_code=HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many concurrent requests. Please try again later."
            )
        await self.semaphore.acquire()

    async def __aexit__(self, exc_type, exc, tb):
        self.semaphore.release()