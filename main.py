from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from database import db
from database import User
import hashlib

import requests
import json

app = Flask(__name__, static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all()


@app.route('/')
def mainpage():
    return render_template('index.html')

# Connexion en tant que membre
@app.route('/login')
def login():
    
    return render_template('login.html')

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
    
    status = r_pokemon.status_code

    if r_pokemon.status_code == 404:
        return render_template('no_pokemon.html'), 404

    pokemon = r_pokemon.json()
    return render_template('pokemon_description.html', pokemon=pokemon, name=name)


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

# Retourne la recherche   
@app.route('/pokemon/<name>')
def search_pokemon(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    status = r_pokemon.status_code
    pokemon = r_pokemon.json()
    return render_template('pokemon_description.html', pokemon=pokemon, name=name, status=status)    

# Retourne l'API du pokemon avec la methode AJAX
@app.route('/pokemon/details/<name>', methods=["POST"])
def get_details_pokemon(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if r_pokemon.status_code == 404:
        list = {}
        return list

    pokemon = r_pokemon.json()
    return pokemon


# Page d'erreur pour pokemon non trouve
app.route('/no_pokemon')
def pokemon_not_found():
    return render_template('no_pokemon.html')

# Page d'erreur
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

