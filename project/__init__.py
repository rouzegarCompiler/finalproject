from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Development,Production


app = Flask(__name__)
app.config.from_object(Development)

# initilize dependencies
db = SQLAlchemy(app)

# blueprints
from mod_user import user

# register blueprints
app.register_blueprint(user)

from . import views