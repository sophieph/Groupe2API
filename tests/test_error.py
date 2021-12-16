import pytest
from main import app

 # Pokemon
def test_404_error_page():
    test_client = app.test_client()
    response = test_client.get('/poke')
    assert response.status_code == 404 

def test_no_pokemon():
    test_client = app.test_client()
    response = test_client.get('/no_pokemon')
    assert response.status_code == 404