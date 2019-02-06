# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:58 PM
from app import create_app, Config

__author__ = 'Allen LIANG'


if __name__ == '__main__':
    # app.run(debug=True)
    app = create_app(Config)
    app.run(debug=False)
