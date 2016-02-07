'''
The views are the handlers that respond to requests from web browsers or other clients. In Flask handlers are written as Python functions. Each view function is mapped to one or more request URLs.
'''
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

#@app.route('/')
#@app.route('/index')
#def index():
#    user = {'nickname': 'Miguel'} # fake use# fake userr
#    return render_template('index.html',
#                           title='Home',
#                           user=user)

@app.route('/login', methods=['GET', 'POST']) # without specifying the methods, the view would accept GET requests only
def login():
    # Instantiate a form object
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)
