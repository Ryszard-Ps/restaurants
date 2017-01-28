from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)

    return app
