from flask.testing import FlaskClient
from app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_cv_analyze(client: FlaskClient):
    response = client.post('/cv/analyze/', json={"cv_text": "Développeur Python avec 5 ans d'expérience."})
    assert response.status_code == 200
    assert "feedback" in response.json

def test_cv_improve(client: FlaskClient):
    response = client.post('/cv/improve/', json={"cv_text": "Développeur Python avec 5 ans d'expérience."})
    assert response.status_code == 200
    assert "improved_cv" in response.json

