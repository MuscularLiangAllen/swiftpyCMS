# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:56 PM
import datetime

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

__author__ = 'Allen LIANG'

from flask import Flask


# app = Flask(__name__)
# app.config.from_object(Config)
# login = LoginManager(app)
# login.session_protection = "strong"
# login.login_view = 'login'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
# 用户没有login时, 跳转至url_for('login')
login.login_view = 'auth.login'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # 设置session的保存时间
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=4)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.article import bp as article_bp
    app.register_blueprint(article_bp, url_prefix='/article')

    return app

from app import forms

