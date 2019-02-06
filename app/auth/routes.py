# -*- coding: utf-8 -*-
from datetime import datetime

from flask import url_for, flash, render_template
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import redirect

from app import db
from app.auth import bp
from app.forms import LoginForm
from app.models import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.verify_pw(login_form.pw.data):
            login_user(user)
            user.last_active = datetime.now()
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')

    return render_template('auth/login.html', title='Sign In', form=login_form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))