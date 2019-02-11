# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 9:57 PM
from flask import url_for, render_template, flash
from flask_login import current_user, login_required, login_user, logout_user

from app.main import bp

__author__ = 'Allen LIANG'


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('main/index_iframe.html')


@bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('main/welcome_iframe2.html')


