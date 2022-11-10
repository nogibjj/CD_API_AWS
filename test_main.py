"""import testclient for testing"""
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)


def test_root():
    """test root"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, this is scratch of Data Engineering api"
    }
