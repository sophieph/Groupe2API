import pytest
import json
import logging as log
from main import app


def test_logout_without_login():
    tester = app.test_client()
    response = tester.get('/offline')

    assert response.status_code == 302

def test_logout_with_login():
    test_client = app.test_client()
    test_client.set_cookie('/', 'username', 'admin')
    response = test_client.get('/offline')
    assert response.status_code == 302

    response = test_client.get('/')
    assert response.status_code == 200

    cookie = response.headers.getlist('Set-Cookie')
    assert cookie is not None

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
@pytest.mark.parametrize('username, password', [('admin', 'adminadmin'), ('kaya', 'nerd')])
def test_login_param(username, password):
    tester = app.test_client()
    response = tester.post('/login', data = dict(username=username, password=password), follow_redirects=True)
    assert response.status_code == 200
    assert b'Hello' in response.data

# Params
@pytest.mark.parametrize('username, password', [('adminnn', 'adminadmin'), ('wrong', 'wrong')])
def test_login_param_failure(username, password):
    tester = app.test_client()
    response = tester.post('/login', data = dict(username=username, password=password), follow_redirects=True)
    assert response.status_code == 403
    assert b'Hello' in response.data



def test_login_failure():
    tester = app.test_client()
    response = tester.post('/login', data={"username":"adminn", "password":"admin"}, follow_redirects=True)
    assert response.status_code == 403

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
    test_client.set_cookie('/', 'username', 'admin')
    response = test_client.get('/account')
    assert response.status_code == 200
    assert b'Compte' in response.data
    
def test_account_with_param():
    tester = app.test_client()
    response = tester.post('/account', data={"username":"sacha"})
    assert response.status_code == 405


def test_signup():
    tester = app.test_client()
    response = tester.post('/signup',data={
        "username":"sacha",
        "email" : "sacha@pokemon.com",
        "password" : "123456",
        "password_1" : "123456"
    }, follow_redirects=True)
    assert response.status_code == 400

def test_empty_username_signup():
    tester = app.test_client()
    response = tester.post('/signup', data={
        "username" :"",
        "email"    : "sacha@pokemon.com",
        "password" : "123456",
        "password_1" : "123456"
    }, follow_redirects=True)
    assert response.status_code == 400

def test_empty_email_signup():
    tester = app.test_client()
    response = tester.post('/signup', data={
        "username" :"sacha",
        "email"    : "",
        "password" : "123456",
        "password_1" : "123456"
        },
    follow_redirects=True)
    assert response.status_code == 400

def test_empty_password_signup():
   tester = app.test_client()
   response = tester.post('/signup', data={
       "username" :"sacha",
       "email"    : "sacha@pokemon.com",
       "password" : "",
       "password_1" : ""
       }, follow_redirects=True)
   assert response.status_code == 400


def test_favoris_with_account():
    test_client = app.test_client()
    test_client.set_cookie('/', 'username', 'admin')
    response = test_client.get('/favoris/charmeleon')
    assert response.status_code == 302

def test_favoris_without_login():
    test_client = app.test_client()
    response = test_client.get('/favoris/charmeleon')
    assert response.status_code == 500

def test_delete_favoris_with_account():
    test_client = app.test_client()
    test_client.set_cookie('/', 'username', 'admin')
    response = test_client.get('/delete/favoris/charmeleon')
    assert response.status_code == 302

def test_delete_favoris_without_login():
    test_client = app.test_client()
    response = test_client.get('/delete/favoris/charmeleon')
    assert response.status_code == 500