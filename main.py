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

# Accueil de la page web
@app.route('/')
def mainpage():
    username = request.cookies.get('username')
    return render_template('index.html', username=username)


# Formulaire d'inscription
@app.route('/signup')
def formulaire():
    username = request.cookies.get('username')
    return render_template('formulaire.html', username=username)

# Formulaire d'inscription
@app.route('/signup', methods=["POST"])
def request_signup():
    username = request.cookies.get('username')
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    password_1 = request.form["password_1"]
    if username == "" or email == "" or password == "" :
        return render_template("formulaire.html", error="Remplissez tous les champs", username=username)

    if password != password_1: 
        return render_template("formulaire.html", error="Mot de passe différent")

    db = get_db()
    r_username = db.get_user(username)
    if r_username is None:
        db.insert_user(username, email, password)
        return render_template('formulaire.html', success="Vous etes inscrits!", username=username)
    else:
        return render_template('formulaire.html', existing="Inscrivez un autre pseudo", username=username)

# Connexion en tant que membre
@app.route('/login')
def login():
    username = request.cookies.get('username')
    if username is not None:
        response = make_response(redirect(url_for('mainpage')))
        return response
    return render_template('login.html', username=username)
    


# Requete pour se connecter
@app.route('/login', methods=["POST"])
def request_login():
    username = request.cookies.get('username')
    if username is not None:
        response = make_response(redirect(url_for('mainpage')))
        return response

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

# Acceder au compte 
@app.route('/account')
def account():
    username = request.cookies.get('username')
    if username is None:
        response = make_response(
            redirect(url_for('mainpage',
                             no_username='no username')))
        return response

    db = get_db()
    id_user = db.get_user_id(username)
    list_favorites = db.get_all_pokemon(id_user)
    print(list_favorites)

    return render_template('compte.html', username=username, list=list_favorites)

#Affiche la liste des 151 premiers Pokemon
@app.route('/pokemon')
def pokemon():
    username = request.cookies.get('username')

    # Liste des 151 premiers pokemon
    try:
        r_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
        list_pokemon = r_pokemon.json()
        pokemon = list_pokemon['results']

        return render_template('pokemon.html', pokemon=pokemon, username=username)
    except :
        # raise SystemExit()
        return redirect((url_for('pokemon_not_found')))


# Affiche la description du pokemon    
@app.route('/pokemon/<name>')
def pokemon_by_name(name):
    username = request.cookies.get('username')
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

    if username is None:
        return render_template('pokemon_description.html', pokemon=pokemon, pokemon_description=pokemon_description, name=name) 
    
    db = get_db()
    id_user = db.get_user_id(username)
    r_favorites = db.get_pokemon(name)

    if r_favorites is None:
        return render_template('pokemon_description.html', pokemon=pokemon, 
                            pokemon_description=pokemon_description, name=name,
                            username=username, favorite='Ajouter aux favoris!')
    
    return render_template('pokemon_description.html', pokemon=pokemon, 
                            pokemon_description=pokemon_description, name=name,
                            username=username, delete_favorite='Supprimer des favoris') 

# Ajoute un pokemon en favoris    
@app.route('/favoris/<name>')
def favoris(name):
    username = request.cookies.get('username')

    db = get_db()
    id_user = db.get_user_id(username)
    r_favorites = db.get_pokemon(name)

    if r_favorites is None:
        db.insert_favorites(name, id_user)
        response = make_response(redirect(url_for('pokemon_by_name', name=name)))
        return response
    
    response = make_response(redirect(url_for('account')))
    response.set_cookie('username', username)
    return response

# Supprime un pokemon des favoris
@app.route('/delete/favoris/<name>')
def delete_favoris(name):
    username = request.cookies.get('username')

    db = get_db()
    id_user = db.get_user_id(username)
    db.delete_pokemon(name, id_user)

    response = make_response(redirect(url_for('pokemon_by_name', name=name)))
    return response

# Affiche le comparatif entre pokémon
@app.route('/comparatif')
def compare_pokemon():
    username = request.cookies.get('username')

    url = 'https://pokeapi.co/api/v2/pokemon/?limit=151'
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    pokemon = r_pokemon.json()
    pokemon = pokemon['results']
    return render_template('comparatif.html', pokemon_list=pokemon,username=username)

# Affiche le classement des pokémons selon leur stat
@app.route('/classement')
def classement_pokemon():
    username = request.cookies.get('username')

    return render_template('classement.html', username=username)

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
    username = request.cookies.get('username')

    return render_template('no_pokemon.html', username=username)

# Page d'erreur
@app.errorhandler(404)
def page_not_found(e):
    username = request.cookies.get('username')

    return render_template('404.html', username=username), 404


if __name__ == "__main__":
    app.run(debug=True)

