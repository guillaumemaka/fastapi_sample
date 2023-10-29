import sqlalchemy
from fastapi import Depends, HTTPException
from db.db_setup import get_db
import models
import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def get_events(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(models.Event).offset(skip).limit(limit)
    results = await db.execute(query)
    return results.scalars().all()

async def create_event(db: AsyncSession, event: schemas.EventCreate) -> models.Event:
    new_event = models.Event(**event.model_dump(mode="python"))

    try:
        await db.begin()
        db.add(new_event)
        await db.commit()
        await db.refresh(new_event)
        return new_event
    except sqlalchemy.exc.IntegrityError:
        await db.rollback() 
        raise HTTPException(status_code=400, detail="Event already exists")
    