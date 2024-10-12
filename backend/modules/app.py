import os
from flask import Flask
from flask_cors import CORS 
from .swatches import swatches_blueprint

def create_app():
    app = Flask(__name__)

    app.config['TESTING'] = os.getenv('TESTING', False)
    app.config['DEBUG'] = os.getenv('DEBUG', True)

    CORS(app)

    @app.route('/')
    def index():
        return "This is the kanopi app test by @tawanorg - https://github.com/tawanorg"

    # Register the swatches blueprint API
    app.register_blueprint(swatches_blueprint, url_prefix='/api/swatches')
    # Register the new blueprint here
    # app.register_blueprint(new_blueprint, url_prefix='/api/x-module')

    return app