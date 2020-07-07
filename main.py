from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/pokemon')
def pokemon():
    # Liste des 151 premiers pokemon
    try:
        r_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    list_pokemon = r_pokemon.json()
    return render_template('pokemon.html', list=list_pokemon)
    
if __name__ == "__main__":
    app.run(debug=True)

