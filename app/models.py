# -*- coding: utf-8 -*-
import datetime
import time
import uuid

import shortuuid
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login
import json


def next_uuid():
    return '%015d%s' % ((time.time() * 1000), uuid.uuid4().hex)


def short_uuid():
    return shortuuid.uuid()


def _to_dict(obj, cls):
    d = {}
    for col in cls.__table__.columns:
        v = getattr(obj, col.name)
        d[col.name] = v() if callable(v) else str(v)
    return d


class User(UserMixin, db.Model):
    '''
    id, username, hashed_pw, register_time, last_active
    '''

    id = db.Column(db.String(50), primary_key=True, default=next_uuid)
    username = db.Column(db.String(50), index=True, nullable=False, unique=True)
    hashed_pw = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    register_time = db.Column(db.DateTime, default=datetime.datetime.now)
    # local time, instead of utcnow()
    r'''
    :param type\_: The column's type, indicated using an instance which
          subclasses :class:`~sqlalchemy.types.TypeEngine`.  If no arguments
          are required for the type, the class of the type can be sent
          as well, e.g.::
    '''
    last_active = db.Column(db.DateTime, default=datetime.datetime.now)
    '''
    relationship 的 lazy 属性指定 sqlalchemy 数据库什么时候加载数据：
        select：就是访问到属性的时候，就会全部加载该属性的数据
        joined：对关联的两个表使用联接
        subquery：与joined类似，但使用子子查询
        dynamic：不加载记录，但提供加载记录的查询，也就是生成query对象
    '''
    articles = db.relationship('Article', backref='author', lazy='dynamic')

    # hashing the password via generate_password_hash(method='pbkdf2:sha256')
    def set_password(self, password):
        self.hashed_pw = generate_password_hash(password)

    def verify_pw(self, password):
        return check_password_hash(self.hashed_pw, password)

    def __str__(self):
        return '<User: {0}, ID: {1}>'.format(self.username, self.id)

    __repr__ = __str__

    @property
    def dict(self):
        return _to_dict(self, self.__class__)

    @property
    def json(self):
        return json.dumps(_to_dict(self, self.__class__))


class Article(db.Model):
    id = db.Column(db.String(50), primary_key=True, default=next_uuid)
    title = db.Column(db.String(120), nullable=False)
    intro = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(40), unique=True, nullable=False, default=short_uuid)
    post_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    last_modified = db.Column(db.DateTime)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'))
    category_id = db.Column(db.String(50), db.ForeignKey('category.id'))

    def __str__(self):
        return '<Article: %s>' % self.title

    __repr__ = __str__

    @property
    def dict(self):
        return _to_dict(self, self.__class__)

    @property
    def json(self):
        return json.dumps(_to_dict(self, self.__class__))


class Image(db.Model):
    id = db.Column(db.String(24), primary_key=True, default=short_uuid)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.now)
    local_path = db.Column(db.String(80), unique=True, nullable=False)


class Category(db.Model):
    id = db.Column(db.String(50), primary_key=True, default=next_uuid)
    name = db.Column(db.String(30), nullable=False, unique=True)
    url = db.Column(db.String(40), nullable=False, unique=True)
    weight = db.Column(db.Integer, default=1)
    parent_id = db.Column(db.String(50))
    articles = db.relationship('Article', backref='category', lazy='dynamic')

    def __str__(self):
        return '<Category: {}>'.format(self.name)

    __repr__ = __str__

    @property
    def dict(self):
        return _to_dict(self, self.__class__)

    @property
    def json(self):
        return json.dumps(_to_dict(self, self.__class__))


@login.user_loader
def load_user(id):
    return User.query.get(id)
