# -*- encoding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response

db = SQLAlchemy()

def create_app(config_filename):
    """Crea una instancia de Flask."""
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)
    
    # Blueprints
    from api.v1.views import restaurants
    app.register_blueprint(restaurants, url_prefix='/api/v1/restaurants')

    return app
