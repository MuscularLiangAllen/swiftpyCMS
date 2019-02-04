# -*- coding: utf-8 -*-
import datetime
import time
import uuid

from flask_login import UserMixin
from flask_sqlalchemy import Model
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


def next_uuid():
    return '%015d%s' % ((time.time()*1000), uuid.uuid4().hex)


class User(UserMixin, Model):
    id = db.Column(db.String(50), primary_key=True, default=next_uuid)
    username = db.Column(db.String(50), index=True, unique=True)
    hashed_pw = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    register_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # local time, instead of utcnow()
    last_active = db.Column(db.DateTime, default=datetime.datetime.now())

    # hashing the password via generate_password_hash(method='pbkdf2:sha256')
    def set_password(self, password):
        self.hashed_pw = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_pw, password)

    def __str__(self):
        return '<User: %s>' % self.username

    __repr__ = __str__


@login.user_loader
def load_user(id):
    return User.query.get(id)