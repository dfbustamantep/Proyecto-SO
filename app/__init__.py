from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    bootstrap = Bootstrap(app)
    return app