import pytest
from fastapi.testclient import TestClient 

@pytest.mark.usefixtures("client")
def test_read_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 404
    # assert response.json() == {"message": "Hello World"}
    