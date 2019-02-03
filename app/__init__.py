# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:56 PM
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

__author__ = 'Allen LIANG'

from flask import Flask


app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.main import forms

