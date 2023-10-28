from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_setup import get_db
from schemas import Event, EventCreate
from operations.events import get_events, create_event

router = APIRouter(
    prefix='/events',
    tags=['events']
)

@router.get('/', response_model=Optional[List[Event]])
async def get_all_events(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    events = await get_events(db, skip, limit)
    return events

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Event)
async def post_event(event: EventCreate, db: AsyncSession = Depends(get_db)):
    event = await create_event(db, event)
    return event