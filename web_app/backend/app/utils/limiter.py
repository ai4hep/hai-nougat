import asyncio
from fastapi import HTTPException
from starlette.status import HTTP_429_TOO_MANY_REQUESTS


class ConcurrencyLimiter:
    """
    Context manager for limiting concurrent requests.
    """

    def __init__(self, semaphore: asyncio.Semaphore):
        self.semaphore = semaphore

    async def __aenter__(self):
        """
        Acquire semaphore on entry.
        Raise HTTPException if semaphore is locked.
        """
        if self.semaphore.locked():
            raise HTTPException(
                status_code=HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many concurrent requests. Please try again later."
            )
        await self.semaphore.acquire()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """
        Release semaphore on exit.
        """
        self.semaphore.release()
