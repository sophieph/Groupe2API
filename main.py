from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import make_response
import hashlib
from database import Database
from flask import url_for

import requests
import json

app = Flask(__name__, static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

# Connexion à la base de données
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.deconnection()

@app.route('/')
def mainpage():
    return render_template('index.html')


# Formulaire d'inscription
@app.route('/signup')
def formulaire():
    return render_template('formulaire.html')

# Formulaire d'inscription
@app.route('/signup', methods=["POST"])
def request_signup():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    password_1 = request.form["password_1"]
    if username == "" or email == "" or password == "" :
        return render_template("formulaire.html", error="Remplissez tous les champs")

    if password != password_1: 
        return render_template("formulaire.html", error="mot de passe différent")
    db = get_db()
    r_username = db.get_user(username)
    if r_username is None:
        db.insert_user(username, email, password)
        return render_template('formulaire.html', success="Vous etes inscrits!")
    else:
        return render_template('formulaire.html', existing="Inscrivez un autre pseudo")

# Connexion en tant que membre
@app.route('/login')
def login():
    return render_template('login.html')

# Requete pour se connecter
@app.route('/login', methods=["POST"])
def request_login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "" or password == "" :
        return render_template("login.html", error="Remplissez tous les champs")

    db = get_db()
    r_username = db.get_user(username)
    if r_username is None:
        return render_template('login.html', no_account="Inscrivez-vous d'abord")

    response = make_response(redirect(url_for('account')))
    response.set_cookie('username', username)
    return response

# Deconnexion
@app.route('/offline')
def offline():
    response = make_response(redirect(url_for('mainpage')))
    response.set_cookie('username', expires=0)
    return response


# Acceder a mon compte 
@app.route('/account')
def account():
    username = request.cookies.get('username')
    if username is None:
        response = make_response(
            redirect(url_for('mainpage',
                             no_username='no username')))
        return response
    return render_template('compte.html', username=username)

#Affiche la liste des 151 premiers Pokemon
@app.route('/pokemon')
def pokemon():
    # Liste des 151 premiers pokemon
    try:
        r_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
        return page_not_found(e)

    list_pokemon = r_pokemon.json()
    pokemon = list_pokemon['results']

    return render_template('pokemon.html', pokemon=pokemon)
    

# Affiche la description du pokemon    
@app.route('/pokemon/<name>')
def pokemon_by_name(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    url_description = 'https://pokeapi.co/api/v2/pokemon-species/' + name
    try:
        r_pokemon_description = requests.get(url_description)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    pokemon = r_pokemon.json()
    pokemon_description = r_pokemon_description.json()
    pokemon_description = pokemon_description

    return render_template('pokemon_description.html', pokemon=pokemon, pokemon_description=pokemon_description, name=name) 


# Affiche le comparatif entre pokémon
@app.route('/comparatif')
def compare_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=151'
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    pokemon = r_pokemon.json()
    pokemon = pokemon['results']
    return render_template('comparatif.html', pokemon_list=pokemon)

# Affiche le classement des pokémons selon leur stat
@app.route('/classement')
def classement_pokemon():

    return render_template('classement.html')

# Retourne l'API du pokemon avec la methode AJAX
@app.route('/pokemon/details/<name>', methods=["POST"])
def get_details_pokemon(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if r_pokemon.status_code == 400:
        list = {}
        return list
    elif r_pokemon.status_code == 404:
        list = {}
        return list

    pokemon = r_pokemon.json()
    return pokemon

# Page d'erreur pour pokemon non trouve
@app.route('/no_pokemon')
def pokemon_not_found():
    return render_template('no_pokemon.html')


# Page d'erreur
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

