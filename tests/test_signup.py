import pytest
from main import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200


# Formulaire d'inscription
def test_signup():
    tester = app.test_client()
    response = tester.post('/pokemon/details/undefined', data={"username":"sacha", "email" : "sacha@pokemon.com", "password" : "123456", "password" : "123456"}, follow_redirects=True)
    assert response.status_code == 200


