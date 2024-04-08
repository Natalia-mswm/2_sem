from fastapi.testclient import TestClient
from hw3_popova import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict():
    response = client.post("/predict/", json={"text": "I love this product"})
    assert response.status_code == 200
    assert "label" in response.json()
    assert "score" in response.json() 
