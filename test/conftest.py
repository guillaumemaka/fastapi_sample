from asyncio import AbstractEventLoop, get_event_loop_policy
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, AsyncIterator, Generator
from db.db_setup import get_db
from db_setup import AsyncTestSessionLocal, get_test_db
from main import app
from fastapi.testclient import TestClient
import pytest
import pytest_asyncio

app.dependency_overrides[get_db] = get_test_db

@pytest_asyncio.fixture
async def db() -> AsyncIterator[AsyncSession]:
    async with AsyncTestSessionLocal() as _db:
        yield _db
        await _db.close()

@pytest.fixture
def client() -> TestClient:
    with TestClient(app) as _client:
        return _client

@pytest.fixture(scope="session")
def async_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(app=app, base_url="http://testserver", follow_redirects=True)

@pytest.fixture(scope="session", autouse=True)
def event_loop() -> Generator["AbstractEventLoop", Any, None]:
    policy = get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()