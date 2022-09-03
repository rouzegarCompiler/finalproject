from flask import request, render_template, flash, redirect, url_for

from flask_login import login_user, login_required, logout_user, current_user

from project import db

from . import user
from .models import User
from .forms import RegisterForm, LoginForm, SqlInjectionForm, SqlInjectionLoginForm
from .utils import user_only, no_login
from .sqlinjection import SqlInjection


@user.route('/')
@login_required
@user_only
def index():
    return render_template('user/index.html', title='User Dashboard')


@user.route('/register', methods=['GET', 'POST'])
@no_login
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
@no_login
def login():
    if current_user.is_authenticated:
        flash('You have already logined .', category='warning')
        return redirect(url_for('user.index'))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter(User.email == form.email.data).first()
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('user.index'))
        flash('Something wrong in your form. Correct these errors and sent form again',
              category='danger')
    return render_template('user/login.html', form=form, title='Login User')


@user.route('/logout')
@login_required
@user_only
def logout():
    logout_user()
    flash('You logged out successfully .', category='warning')
    return redirect(url_for('user.login'))


@user.route('/sqlinjection/with-login', methods=['GET', 'POST'])
@login_required
@user_only
def sqlinjection_login():
    form = SqlInjectionLoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            sqli = SqlInjection()
            login = sqli.login(form.login_url.data, form.login_query.data, int(
                form.form_number.data), form.login_response.data)
            if login:
                errors = sqli.run(form.url.data, form.base_url.data)
                return render_template('user/sqlinjection_with-login.html', form=form, errors=errors, title='SQL Injection - With Login')
            return redirect(url_for('user.sqlinjection_login'))
        flash('Something wrong in your form. Correct these errors and sent form again',
              category='danger')

    return render_template('user/sqlinjection_with-login.html', form=form, title='SQL Injection - With Login')


@user.route('/sqlinjection/without-login', methods=['GET', 'POST'])
@login_required
@user_only
def sqlinjection_nologin():
    form = SqlInjectionForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            sqli = SqlInjection()
            errors = sqli.run(form.url.data, form.base_url.data)
            return render_template('user/sqlinjection_without-login.html', form=form, errors=errors, title='SQL Injection - Without Login')
        flash('Something wrong in your form. Correct these errors and sent form again',
              category='danger')

    return render_template('user/sqlinjection_without-login.html', form=form, title='SQL Injection - Without Login')
