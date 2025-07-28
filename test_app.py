import pytest
from app import app  # Make sure your main file is named `app.py`

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Deepali's Portfolio" in response.data

def test_info_page(client):
    response = client.get('/info')
    assert response.status_code == 200
    assert b"Deepali Pateriya" in response.data

def test_projects_page(client):
    response = client.get('/projects')
    assert response.status_code == 200
    assert b"My Projects" in response.data

def test_social_page(client):
    response = client.get('/social')
    assert response.status_code == 200
    assert b"My Social Media" in response.data
	