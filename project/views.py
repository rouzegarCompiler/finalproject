from urllib.parse import urldefrag
from flask import render_template, redirect, url_for

from flask_login import login_required, current_user

from . import app


@app.route('/')
def index():
    return redirect(url_for('user.login'))