# tests/test_main.py
from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_create():
    payload = {"name": "string", "description": "string", "price": 0, "tax": 3.2}

    response = client.post("/items/", json=payload)

    assert response.status_code == 200, response.text

    data = response.json()
    assert data["item"]["name"] == payload["name"]

    print(response.json())

def test_read():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert "item_id" in data
