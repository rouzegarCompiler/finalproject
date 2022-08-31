from project import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    fname = db.Column(db.String(length = 24), nullable = False)
    lname = db.Column(db.String(length = 24), nullable = False)
    email = db.Column(db.String(length = 160), nullable = False , unique = True)
    gender = db.Column(db.Integer(), nullable = False)
    role = db.Column(db.Integer(), nullable = False, default = 0)