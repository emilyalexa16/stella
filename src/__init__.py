import os
from dotenv import load_dotenv

from flask import Flask

load_dotenv()

UPLOAD_DEST = 'uploads.txt'

def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'dev'
    app.config['UPLOAD_DEST'] = UPLOAD_DEST

    if test_config:
        app.config.from_mapping(test_config)

    from .routes import main
    app.register_blueprint(main.bp)  

    from .routes import categories
    app.register_blueprint(categories.bp)

    from .routes import about
    app.register_blueprint(about.bp) 
       
    from .routes import contact
    app.register_blueprint(contact.bp)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

    return app