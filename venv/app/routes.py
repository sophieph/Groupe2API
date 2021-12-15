from flask import render_template, flash, redirect, url_for
from flask import request
from app import app
from app.forms import LoginForm
from app.pokemonClass import Pokemon

@app.route('/')
@app.route('/index')
def index():
    username = request.cookies.get('username')
    return render_template('index.html', username=username)
    # user = {'username': 'Miguel'}
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    # return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

#Affiche la liste des 151 premiers Pokemon
@app.route('/pokemon')
def listPok():
    p = Pokemon()
    p.attrapezLesTous()

