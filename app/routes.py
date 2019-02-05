# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:57 PM
from flask import url_for, render_template, request, flash
from flask_login import current_user, login_required, login_user
from werkzeug.utils import redirect

from app import app
from app.main.forms import LoginForm
from app.models import User

__author__ = 'Allen LIANG'


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('main/index_iframe.html')


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    print('dashboard invokde...')
    return render_template('main/welcome_iframe.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(login_form.pw.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')

    return render_template('auth/login.html', title='Sign In', form=login_form)
