from fastapi.testclient import TestClient

from main import app


def test_health_and_root_endpoints():
    client = TestClient(app)
    assert client.get('/health').status_code == 200
    assert client.get('/').status_code == 200
