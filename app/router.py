import asyncio
from asyncio import Lock, Semaphore
from time import monotonic

from fastapi import APIRouter

from app.schemas import TestResponse

router = APIRouter(prefix='/test', tags=['Test'])

lock = Lock()
async def work() -> None:
    async with lock:
        await asyncio.sleep(3)


@router.get('', response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    await work()
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)



#Вариант с семафорой
#semaphore = Semaphore(1)
# async def work() -> None:
#     async with semaphore:
#         await asyncio.sleep(3)
#

