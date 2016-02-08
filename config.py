import os

SRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
        {'name': 'Google',   'url': 'https://www.google.com/accounts/o8/id'},            
        {'name': 'Yahoo',    'url': 'https://me.yahoo.com'},
        {'name': 'AOL',      'url': 'http://openid.aol.com/<username>'},
        {'name': 'Flickr',   'url': 'http://www.flickr.com/<username>'},
        {'name': 'MyOpenId', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI is required by the Flask-SQLAlchemy extension.
# It is the path for the database file.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# The SQLALCHEMY_MIGRATE_REPO is the folder where to store the SQLAlchemy-migrate
# data files.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
