# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 10:05 PM
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

__author__ = 'Allen LIANG'


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    pw = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign In')


class ArticleForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    author = StringField('Author')
    intro = StringField('Intro', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    url = StringField('URL')
    submit = SubmitField('Submit')
