from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
# TODO what exactly should my secret key look like?
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
