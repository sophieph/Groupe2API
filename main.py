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
    r = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=100&offset=20')

    list = r.json()
    return render_template('pokemon.html', list=list)
    
if __name__ == "__main__":
    app.run(debug=True)

