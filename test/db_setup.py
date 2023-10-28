import os
from typing import Iterator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', "sqlite:///./test.db")

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
)

AsyncTestSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

async def get_test_db():
    async with AsyncTestSessionLocal() as _db:
        yield _db
