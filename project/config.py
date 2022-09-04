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


class ProductionDB:
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_PORT = os.environ.get('MYSQL_PORT')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')

class Production(Config):
    # For Flask_SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{ProductionDB.MYSQL_USER}:{ProductionDB.MYSQL_PASSWORD}@{ProductionDB.MYSQL_HOST}:{ProductionDB.MYSQL_PORT}/{ProductionDB.MYSQL_DATABASE}'
    SQLALCHEMY_ECHO = False
