# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:56 PM

__author__ = 'Allen LIANG'

from flask import Flask


app = Flask(__name__)

from app.main import routes