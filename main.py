from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__, static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def hello():
    return render_template('index.html')

#Affiche la liste des 151 premiers Pokemon
@app.route('/pokemon')
def pokemon():
    # Liste des 151 premiers pokemon
    try:
        r_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    list_pokemon = r_pokemon.json()
    pokemon = list_pokemon['results']

    return render_template('pokemon.html', pokemon=pokemon)
    
#Affiche les images de la liste avec la methode AJAX
@app.route('/pokemon/image/<name>', methods=["POST"])
def get_image_pokemon(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    pokemon = r_pokemon.json()
    return pokemon




# Affiche la description du pokemon    
@app.route('/pokemon/<name>')
def pokemon_by_name(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    try:
        r_pokemon = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

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

if __name__ == "__main__":
    app.run(debug=True)

