# app.py

from flask import Flask
from werkzeug.urls import quote as url_quote
from urllib.parse import quote as url_quote

# In app.py
from application.utilities import helper_function

# Use the helper function
result = helper_function()



def create_app():
    app = Flask(__name__)

    # Import blueprints lazily to avoid circular import
    from .application.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    # Import models after app creation to avoid circular import
    from . import models

    return app
