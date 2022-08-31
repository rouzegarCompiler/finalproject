from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Development,Production
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Development)

# initilize dependencies
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# blueprints
from project.mod_user import user

# register blueprints
app.register_blueprint(user)

from . import views