# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 10:05 PM
from flask_wtf import FlaskForm
from wtforms import StringField

__author__ = 'Allen LIANG'


class LoginForm(FlaskForm):
    username = StringField()
    pw = StringField()
    hash_pwd = StringField()
    email = StringField()
    # last_avtive =