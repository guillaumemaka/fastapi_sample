from typing import Any, Dict
from faker import Faker
import httpx
import models
import pytest_anyio
from sqlalchemy.ext.asyncio import AsyncSession
import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from datetime import datetime

@pytest.fixture
def create_event(faker: Faker) -> Dict[str, Any]:
    event_name = "Event Name %s" % str(faker.random_int(0, 100))
    return {
        "name": event_name,
        "description": "Event Description",
        "event_timestamp": datetime.utcnow(),
        "location": "Event Location",
        "event_status": faker.random_int(0, 100),
        "event_type": "Event Type",
    }

@pytest.fixture
def create_event_json(faker: Faker) -> Dict[str, Any]:
    event_name = "Event Name %s" % str(faker.random_int(0, 100))
    return {
        "name": event_name,
        "description": "Event Description",
        "event_timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "location": "Event Location",
        "event_status": faker.random_int(0, 100),
        "event_type": "Event Type",
    }

@pytest_asyncio.fixture
async def create_random_event(db: AsyncSession, create_event: Dict[str, Any]):
    event = models.Event(**create_event)
    
    db.add(event)
    
    await db.commit()
    await db.refresh(event)
    
    yield event
    
    await db.delete(event)
    await db.commit()
    await db.close()

def test_get_events_endpoint(client: TestClient, create_random_event: models.Event):
    response = client.get("/events")
    
    assert response.status_code == 200
    
    event = response.json()[0]
    
    assert event["name"] == create_random_event.name
    assert event["description"] == create_random_event.description
    assert event["event_timestamp"] != None
    assert event["location"] == create_random_event.location
    assert event["event_type"] == create_random_event.event_type
    assert event["event_status"] == create_random_event.event_status
    assert event["event_type"] == create_random_event.event_type

@pytest.mark.asyncio
async def test_post_return_201(async_client: httpx.AsyncClient, create_event_json: Dict[str, Any]):
    response = await async_client.post(
        "/events",
        json=create_event_json
    )
    
    assert response.status_code == 201