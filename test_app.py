from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')

    assert response._status_code == 200
    assert b"CICD pipeline working!" in response.data