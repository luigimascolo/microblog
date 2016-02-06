from flask import Flask

app = Flask(__name__)
from app import views # do not confuse app variable with app module

