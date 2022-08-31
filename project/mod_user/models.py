from werkzeug.security import generate_password_hash, check_password_hash
from project import db


class User(db.Model):
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