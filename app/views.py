'''
The views are the handlers that respond to requests from web browsers or other clients. In Flask handlers are written as Python functions. Each view function is mapped to one or more request URLs.
'''
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Zaphod'} # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

# without specifying the methods, the view would accept GET requests only
@app.route('/login', methods=['GET', 'POST']) 
def login():
    # Instantiate a form object
    form = LoginForm()
    # Handling submitted data: validate and store the form data
    if form.validate_on_submit():
        # The flash function provides feedback to the user.
        # Show a message on the next page containing the submitted data
        flash('Login requested for OpenID="%s", remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    # If data are not validated or not inserted, return the login page
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
