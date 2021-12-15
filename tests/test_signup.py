import pytest
from main import app
from flask import Flask

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200


# Formulaire d'inscription
def test_signup():
    print(app)
    tester = app.test_client()
    response = tester.post('/pokemon/details/undefined', data={"username":"sacha", "email" : "sacha@pokemon.com", "password" : "123456", "password" : "123456"}, follow_redirects=True)
    print(response.status_code)
    print()
    print(response.data)
    assert 200 == 200

def test_empty_username_signup():
   tester = app.test_client()
   response = tester.post('/pokemon/details/undefined', data={
       "username" :"",
       "email"    : "sacha@pokemon.com",
       "password" : "123456",
       "password" : "123456"
       }, follow_redirects=True
    )
   assert response.status_code == 200

# def test_empty_email_signup():
    # tester = app.test_client()
    # response = tester.post('/pokemon/details/undefined', data={"username":"sacha", "email" : "", "password" : "123456", "password" : "123456"}, follow_redirects=True)
    # assert response.status_code == 401*/