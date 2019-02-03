# -*- coding: utf-8 -*-
from flask_login import UserMixin
from flask_sqlalchemy import Model

from app import db


class User(UserMixin, Model):
    id = db.Column()