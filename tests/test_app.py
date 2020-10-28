from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"payload": "Hello World!"}


def test_get_table():
    response = client.get("/table")
    assert response.status_code == 200


def test_post_table():
    response = client.post(
        "/table", json={"name": "test", "email": "test@gmail.com"})
    assert response.status_code == 200


def test_post_table_no_email():
    response = client.post("/table", json={"name": "test"})
    assert response.status_code == 422


def test_post_table_no_name():
    response = client.post("/table", json={"email": "test"})
    assert response.status_code == 422


def test_get_weather():
    response = client.get("/weather")
    assert response.status_code == 200
