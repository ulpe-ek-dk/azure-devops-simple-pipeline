import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hent_vindmoeller(client):
    response = client.get('/api/vindmoeller')
    assert response.status_code == 200

def test_hent_enkelt_vindmoelle(client):
    response = client.get('/api/vindmoeller/1')
    assert response.status_code == 200

def test_vindmoelle_ikke_fundet(client):
    response = client.get('/api/vindmoeller/999')
    assert response.status_code == 404
