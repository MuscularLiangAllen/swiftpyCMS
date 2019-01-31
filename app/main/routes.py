# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:57 PM
from app.main import app

__author__ = 'Allen LIANG'


@app.route('/')
@app.route('/index')
def index():
    print('index invoked...')
    return 'hello flask'

