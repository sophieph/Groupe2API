import pytest
from main import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_comparatif():
    test_client = app.test_client()
    response = test_client.get('/comparatif')
    assert response.status_code == 200    

def test_classement():
    test_client = app.test_client()
    response = test_client.get('/classement')
    assert response.status_code == 200  
    assert b'Classement' in response.data
