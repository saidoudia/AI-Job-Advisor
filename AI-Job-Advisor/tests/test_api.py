from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_cv():
    response = client.get("/cv/")
    assert response.status_code == 200
    assert response.json() == {"message": "Voici le CV"}
