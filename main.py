from fastapi import FastAPI
from api import events


app = FastAPI(
    title="FastAPI with SQLAlchemy",
    description="A simple example of FastAPI with SQLAlchemy",
    version="1.0.0",
)

app.include_router(events.router)