import os

class Config:
    # For Flask Application
    SECRET_KEY = 'Secret_key'

    # For Flask_SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    # For Flask_SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_ECHO = True

class Production(Config):
    # For Flask_SQLALCHEMY
    SQLALCHEMY_ECHO = False