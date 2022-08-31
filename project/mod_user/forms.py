from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, RadioField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from .models import User


class RegisterForm(FlaskForm):
    fname = StringField(
        label='First name',
        validators=[DataRequired(), Length(max=24)]
    )
    lname = StringField(
        label='Last name',
        validators=[DataRequired(), Length(max=24)]
    )
    email = EmailField(
        label='Email',
        validators=[DataRequired(), Email(), Length(max=160)]
    )
    password = PasswordField(
        label='Password',
        validators=[DataRequired()]
    )
    password_confirm = PasswordField(
        label='Confirm password',
        validators=[EqualTo('password')]
    )
    gender = RadioField(
        label='Gender',
        choices=[(1, 'Male'), (2, 'Female')],
    )
    submit = SubmitField(label='Register')

    def validate_email(self, email):
        if User.query.filter(User.email == email.data).first():
            raise ValidationError('Email duplicated .Try another email .')
