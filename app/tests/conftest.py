from typing import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import create_app


@pytest.fixture(scope='function')
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=create_app()), timeout=100.0, base_url='http://test') as ac:
        yield ac