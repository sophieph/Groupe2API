import pytest
import json
import logging as log
from main import app


def test_logout_without_login():
    tester = app.test_client()
    response = tester.get('/offline')

    assert response.status_code == 302


# LOGIN 
def test_login():
    tester = app.test_client()
    response = tester.post('/login', data={"username":"admin", "password":"adminadmin"}, follow_redirects=True)
    assert response.status_code == 200
    assert b'<form' in response.data
    assert b'<input' in response.data 

    cookie = response.headers.getlist('Set-Cookie')

    assert cookie is not None


# Params
@pytest.mark.parametrize('username, password', [('admin', 'adminadmin'), ('wrong', 'wrong')])
def test_login_param(username, password):
    tester = app.test_client()
    response = tester.post('/login', data = dict(username=username, password=password), follow_redirects=True)
    assert response.status_code == 200
    assert b'Hello' in response.data



def test_login_failure():
    tester = app.test_client()
    response = tester.post('/login', data={"username":"adminn", "password":"admin"}, follow_redirects=True)
    assert response.status_code == 200

# def test_signup():
#     tester = app.test_client()
#     response = tester.post('/signup', data={"username":"test01", "email":"test01@gmail.com", "password":"test01test", "password_01":"test01test"}, follow_redirects=True)
#     assert response.status_code == 200

# Account
def test_account_without_login():
    test_client = app.test_client()
    response = test_client.get('/account')
    assert response.status_code == 302

def test_account_with_login():
    test_client = app.test_client()
    response = test_client.get('/account')
    test_client.set_cookie('/', 'username', 'admin')
    assert b'Compte' in response.data



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

def test_comparatif():
    test_client = app.test_client()
    response = test_client.get('/comparatif')
    assert response.status_code == 200    

def test_comparatif():
    test_client = app.test_client()
    response = test_client.get('/classement')
    assert response.status_code == 200  
    assert b'Classement' in response.data
  
 # Pokemon
def test_404_error_page():
    test_client = app.test_client()
    response = test_client.get('/poke')
    assert response.status_code == 404 

def test_no_pokemon():
    test_client = app.test_client()
    response = test_client.get('/no_pokemon')
    assert response.status_code == 200