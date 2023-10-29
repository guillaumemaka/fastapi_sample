import os
from typing import Iterator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', "sqlite:///./test.db")

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    future=True,
)

AsyncTestSessionLocal = async_sessionmaker(async_engine)

async def get_test_db():
    async with AsyncTestSessionLocal() as _db:
        yield _db
        await _db.close()
