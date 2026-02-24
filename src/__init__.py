import os
from dotenv import load_dotenv
import click

from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    if test_config:
        app.config.from_mapping(test_config)
    
    from . import db
    db.init_app(app)

    return app