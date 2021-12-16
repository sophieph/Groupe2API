import pytest
from main import app

# Pokemon
def test_pokemon_not_found():
    test_client = app.test_client()
    response = test_client.get('/pokemon/details/char')
    assert response.status_code == 404

def test_pokemon_found_comparatif():
    test_client = app.test_client()
    response = test_client.post('/pokemon/details/charizard')
    assert response.status_code == 200
    assert b'weight' in response.data
    assert b'ability' in response.data

def test_pokemon_list():
    test_client = app.test_client()
    response = test_client.get('/pokemon')
    assert response.status_code == 200
    assert b'charmeleon' in response.data
    

def test_pokemon_detail():
    test_client = app.test_client()
    response = test_client.get('/pokemon/charizard')
    assert response.status_code == 200

def test_pokemon_detail_not_found():
    test_client = app.test_client()
    response = test_client.get('/pokemon/charizarddd')
    assert response.status_code == 500

