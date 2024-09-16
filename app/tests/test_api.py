import asyncio
import asyncio

import pytest
from httpx import AsyncClient


async def test_concurrent_requests(async_client: AsyncClient):
    tasks = [async_client.get('/test') for _ in range(3)]

    responses = await asyncio.gather(*tasks)
    data = []

    for i, response in enumerate(responses):
        elapsed_time = response.json()['elapsed']
        print(f'Время на {i} запрос: {elapsed_time}')
        data.append(elapsed_time)


    for i in range(1, len(data)):
        assert data[i] - data[i-1] >= 3


