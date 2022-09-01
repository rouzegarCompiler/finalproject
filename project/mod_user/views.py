from flask import request, render_template, flash, redirect, url_for

from project import db

from . import user
from .models import User
from .forms import RegisterForm, LoginForm

from flask_login import login_user, login_required, logout_user


@user.route('/')
@login_required
def index():
    return render_template('user/index.html', title='User Dashboard')


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()

            form.populate_obj(user)

            db.session.add(user)
            db.session.commit()
            # Todo : Redirect to login page
            flash('Account created successfully. Login your account.',
                  category='success')

            return redirect(url_for('user.login'))

        flash('Something wrong in your form. Correct these errors and sent form again',
              category='danger')

    return render_template('user/register.html', form=form, title='Register User')


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()
            login_user(user)
            return redirect(url_for('user.index'))
        flash('Something wrong in your form. Correct these errors and sent form again',
              category='danger')
    return render_template('user/login.html', form=form, title='Login User')


@user.route('/logout')
def logout():
    logout_user()
    flash('You logged out successfully .', category='warning')
    return redirect(url_for('user.login'))
