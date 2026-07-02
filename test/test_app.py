import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert b"Task Manager" in response.data


def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200