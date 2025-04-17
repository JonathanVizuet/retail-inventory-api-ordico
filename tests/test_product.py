from http.client import responses

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products", json= {
        "name": "Camisa",
        "price": 299.00,
        "stock": 198
    })

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Camisa"
    assert data["price"] == 299.00
    assert data["stock"] == 198
    assert "id" in data