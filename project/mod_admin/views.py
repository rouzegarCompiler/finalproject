from flask import render_template, abort, flash, redirect, url_for

from flask_login import login_required

from http import HTTPStatus

from project import db

from . import admin
from .utils import admin_only
from .forms import ActiveUserForm, DeactiveUserForm

from ..mod_user.models import User


@admin.route('/')
@login_required
@admin_only
def index():
    return render_template('admin/index.html', title='Admin Home')


@admin.route('/users')
@login_required
@admin_only
def list_users():
    users = User.query.filter(User.role != 1).all()
    active_form = ActiveUserForm()
    deactive_form = DeactiveUserForm()
    return render_template('admin/list_users.html', users=users, active_form=active_form, deactive_form=deactive_form, title='List Users')


@admin.route('/users/activate/<int:id>', methods=['POST'])
@login_required
@admin_only
def activate_user(id):
    user = User.query.get(id)
    if not user:
        abort(HTTPStatus.NOT_FOUND)
    else:
        if not user.active:
            user.active = True
            db.session.add(user)
            db.session.commit()
            flash(
                f'User \"{user.fname} {user.lname}\" activated .', category='success')
        else:
            flash(
                f'User \"{user.fname} {user.lname}\" already activated .', category='warning')
        return redirect(url_for('admin.list_users'))


@admin.route('/users/deactivate/<int:id>', methods=['POST'])
@login_required
@admin_only
def deactivate_user(id):
    user = User.query.get(id)
    if not user:
        abort(HTTPStatus.NOT_FOUND)
    else:
        if user.active:
            user.active = False
            db.session.add(user)
            db.session.commit()
            flash(
                f'User \"{user.fname} {user.lname}\" deactivated .', category='danger')
        else:
            flash(
                f'User \"{user.fname} {user.lname}\" already deactivated .', category='warning')
        return redirect(url_for('admin.list_users'))


@admin.route('/users/report/<int:id>')
@login_required
@admin_only
def report_user(id):
    return 'report user'
