from flask import abort

from flask_login import current_user

from http import HTTPStatus
from functools import wraps

def admin_only(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if current_user.role != 1:
            abort(HTTPStatus.FORBIDDEN)
        return func(*args,**kwargs)
    return wrapper