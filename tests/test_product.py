from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_product():
    response = client.post(
        "/products", json={"name": "Camisa", "price": 299.00, "stock": 198}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Camisa"
    assert data["price"] == 299.00
    assert data["stock"] == 198
    assert "id" in data


def test_get_product():
    # ESTE TEST TOMA DATOS DE LA BASE DE DATOS. NO ES BUENA PRACTICA PARA CI/CD PERO
    # AQUI TAMBIEN PROBAMOS LA CORRECTA CONEXION A LA BASE DE DATOS POR SER UNA PRUEBA
    response = client.get("/products/2")

    assert response.status_code == 200

    product = response.json()
    assert product["id"] == 2
    assert product["name"] == "Camisa"
    assert product["price"] == 299
    assert product["stock"] == 198


def test_update_stock():
    product_id = 1
    nuevo_stock = 19
    response = client.put(f"/products/{product_id}", params={"stock": nuevo_stock})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["stock"] == nuevo_stock


def test_delete_product():
    # Aquí se va crear un nuveo producto para eliminar después
    create_response = client.post(
        "/products", json={"name": "Temporal", "price": 99, "stock": 9}
    )
    assert create_response.status_code == 200
    created_product = create_response.json()
    product_id = created_product["id"]

    # Aquí lo eliminamoas:
    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"detail": "Producto eliminado correctamente"}

    # y aqui verificamsoq que no exista ya:
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404
