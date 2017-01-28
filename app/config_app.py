# -*- encoding: utf-8 -*-
# Variables Flask
import os

PORT = 5000
HOST = "0.0.0.0"
SECRET_KEY = 'dsDS323js73hshdsjASDFAs'

# Variables SQLALCHEMY
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Variable de conexión de SQLALCHEMY
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
