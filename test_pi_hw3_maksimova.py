from fastapi.testclient import TestClient
from pi_hw3_maksimova import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_get_info():
    response = client.get("/translate/")
    assert response.status_code == 200
    assert response.json() == [{"translation_text":"Ça ne fut pas si facile."}]
