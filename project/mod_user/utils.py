from flask import redirect, url_for

from flask_login import current_user

from functools import wraps

from project import db

from .models import AttackWeb


def user_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.role == 1:
            return redirect(url_for('admin.index'))
        return func(*args, **kwargs)
    return wrapper


def no_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('user.index'))
        return func(*args, **kwargs)
    return wrapper

def add_attack(type_,url,use_login):
    attack = AttackWeb(type_=type_,url=url,use_login=use_login)
    attack.attacker = current_user
    db.session.commit()