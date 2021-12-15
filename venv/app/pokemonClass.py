from flask import render_template, redirect, url_for
from flask import request
import requests

class Pokemon:
    
    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        pass
    
    def attrapezLesTous():
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