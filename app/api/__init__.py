from flask import Flask, Response


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    return app
