from flask import Flask
from .config import Development,Production

app = Flask(__name__)
app.config.from_object(Development)

from . import views