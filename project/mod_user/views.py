from flask import request, render_template, flash

from project import db

from . import user
from .models import User
from .forms import RegisterForm


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

            return 'Created User'

        flash('Something wrong in your form. Correct these errors and sent form again',category='danger')

    return render_template('user/register.html', form=form, title='Register User')
