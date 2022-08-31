from werkzeug.security import generate_password_hash, check_password_hash

from project import db
from project import login

from flask_login import UserMixin


class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    fname = db.Column(db.String(length=24), nullable=False)
    lname = db.Column(db.String(length=24), nullable=False)
    email = db.Column(db.String(length=160), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=200), nullable=False)
    gender = db.Column(db.Integer(), nullable=False)
    role = db.Column(db.Integer(), nullable=False, default=0)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password_):
        self.password_hash = generate_password_hash(password_)

    def check_password(self, password_):
        return check_password_hash(self.password_hash,password_)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))