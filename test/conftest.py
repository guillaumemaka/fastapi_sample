import pytest_asyncio
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncIterator, Iterator
from db.db_setup import get_db
from db_setup import AsyncTestSessionLocal, get_test_db
from main import app
from fastapi.testclient import TestClient
import pytest

app.dependency_overrides[get_db] = get_test_db

@pytest_asyncio.fixture
async def db() -> AsyncIterator[AsyncSession]:
    async with AsyncTestSessionLocal() as _db:
        yield _db
        
        if _db.is_active:
            await _db.close()

@pytest.fixture
def client() -> TestClient:
    with TestClient(app) as _client:
        return _client

@pytest.fixture
def async_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(app=app, base_url="http://testserver", follow_redirects=True)
