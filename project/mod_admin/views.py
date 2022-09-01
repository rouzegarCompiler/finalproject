from flask_login import login_required
from . import admin
from .utils import admin_only


@admin.route('/')
@login_required
@admin_only
def index():
   return 'Admin page'

@admin.route('/users')
@login_required
@admin_only
def list_users():
    return 'List users'

@admin.route('/users/activate/<int:id>')
@login_required
@admin_only
def activate_user(id):
    return 'activate user'

@admin.route('/users/deactivate/<int:id>')
@login_required
@admin_only
def deactivate_user(id):
    return 'deactivate user'

@admin.route('/users/report/<int:id>')
@login_required
@admin_only
def report_user(id):
    return 'report user'
