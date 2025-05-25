"""Basic tests for the FastAPI application."""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    """Test the /health endpoint returns status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_echo():
    """Test the /echo endpoint returns posted data."""
    response = client.post("/echo", json={"msg": "hello"})
    assert response.status_code == 200
    assert response.json() == {"you_sent": {"msg": "hello"}}
