# tests/test_cv.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_cv():
    response = client.post("/cv/analyze/")
    assert response.status_code == 200
    assert response.json() == {"message": "Analyse du CV effectuée"}

def test_improve_cv():
    response = client.post("/cv/improve/")
    assert response.status_code == 200
    assert response.json() == {"message": "Amélioration du CV effectuée"}
