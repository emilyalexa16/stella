import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

UPLOAD_DEST = 'uploads.txt'

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['UPLOAD_DEST'] = UPLOAD_DEST

    if test_config:
        app.config.from_mapping(test_config)
    
    from .db import db
    db.init_app(app)

    from .routes import auth
    app.register_blueprint(auth.bp)

    from .routes import main
    app.register_blueprint(main.bp)  

    from .routes import categories
    app.register_blueprint(categories.bp)

    return app