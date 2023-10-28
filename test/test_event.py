import httpx
from sqlalchemy.ext.asyncio import AsyncSession
import models
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from datetime import datetime

@pytest_asyncio.fixture
async def create_random_event(db: AsyncSession):
    event = models.Event(
        name="Event Name",
        description="Event Description",
        event_timestamp=datetime.fromisoformat("2020-05-01 12:00:00"),
        location="Event Location",
        event_status=1,
        event_type="Event Type",
    )
    
    db.add(event)
    await db.commit()
    await db.refresh(event)
    
    yield event
    
    await db.delete(event)
    await db.commit()
    await db.close()

@pytest.mark.usefixtures("client", "create_random_event")
def test_get_events_endpoint(client: TestClient, create_random_event: models.Event):
    response = client.get("/events")
    
    assert response.status_code == 200
    
    event = response.json()[0]
    
    assert event["id"] == create_random_event.id
    assert event["name"] == create_random_event.name
    assert event["description"] == create_random_event.description
    assert event["event_timestamp"] != None
    assert event["location"] == create_random_event.location
    assert event["event_type"] == create_random_event.event_type
    assert event["event_status"] == create_random_event.event_status
    assert event["event_type"] == create_random_event.event_type

@pytest.mark.asyncio
@pytest.mark.usefixtures("async_client")
async def test_post_return_201(async_client: httpx.AsyncClient):
    response = await async_client.post(
        "/events",
        json={
            "name": "Event Name",
            "description": "Event Description",
            "event_timestamp": "2020-05-01 12:00:00",
            "location": "Event Location",
            "event_status": 1,
            "event_type": "Event Type",
        }
    )
    
    assert response.status_code == 201