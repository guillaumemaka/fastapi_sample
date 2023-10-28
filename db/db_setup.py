import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./sql_app.db')

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={},
    future=True,
)

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()  

async def get_db():
    async with AsyncSessionLocal() as db:
        yield db