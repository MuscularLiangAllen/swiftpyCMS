# -*- coding: utf-8 -*-
import os


class Config:
    SECRET_KEY = os.urandom(24)
    # SQLAlchemy-mysql config
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:mysql57@localhost:3306/swiftpycms_db?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 打印SQL语句
    SQLALCHEMY_ECHO = False

    POSTS_PER_PAGE = 3

    FS_ROOT_DIR = '/swiftpy_fs'
    FS_ROOT_UPLOAD = 'upload'
    FS_ROOT_IMG_UPLOAD = 'img'
    FS_ROOT_FILE_UPLOAD = 'file'

    STATIC_FOLDER = 'static'