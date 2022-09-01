from flask_wtf import FlaskForm
from wtforms import SubmitField


class ActiveUserForm(FlaskForm):
    submit = SubmitField(label='Active')

class DeactiveUserForm(FlaskForm):
    submit = SubmitField(label='Deactive')