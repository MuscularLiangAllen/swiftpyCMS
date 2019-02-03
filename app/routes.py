# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:57 PM
from flask import url_for, render_template, request
from flask_login import current_user, login_required
from werkzeug.utils import redirect

from app import app
from app.main.forms import LoginForm

__author__ = 'Allen LIANG'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    print('index invoked...')
    return 'hello flask'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print('submit invoked...')

        return redirect(url_for('index'))

    return render_template('auth/login.html', title='Sign In', form=login_form)
