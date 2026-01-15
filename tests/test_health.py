import pytest 
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "devops-demo"


def test_status_endpoint(client):
    response = client.get("/status")
    assert response.status_code == 200

    data = response.get_json()
    assert "uptime_seconds" in data
    assert "environment" in data


    