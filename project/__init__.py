from flask import Flask

from .config import Development,Production

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Development)

# initilize dependencies
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# set param for extentions
login.login_view = 'user.login'
login.login_message_category = 'danger'

# blueprints
from project.mod_user import user
from project.mod_admin import admin

# register blueprints
app.register_blueprint(user)
app.register_blueprint(admin)

from . import views