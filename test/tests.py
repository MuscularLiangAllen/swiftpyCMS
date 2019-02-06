# -*- coding: utf-8 -*-
import datetime
import random
import uuid

import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db, models, create_app, Config
from app.models import User, Article


class Test:
    def __init__(self, time, time_default=datetime.datetime.now):
        if time is None and callable(time_default):
            print(time_default())


if __name__ == '__main__':
    # print(len(uuid.uuid4().hex))
    # uuid4 = uuid.uuid4()
    # print(uuid4)
    # print(uuid4.hex)
    # print(str(uuid4).replace('-', ''))
    # print(time.time())
    # print(datetime.datetime.timestamp(datetime.datetime.now()))
    # print('%015d%s'%((time.time()*1000), uuid4.hex))
    # print(len('%015d%s'%((time.time()*1000), uuid4.hex)))
    #
    # u = User()
    # print(type(u))
    # from app.models import User
    #
    # u1 = User(username='kingroot', email='liangtee@126.com')
    # u1.set_password('kingroot')
    # db.session.add(u1)
    # db.session.commit()
    # import shortuuid
    # for i in range(10):
    #     print(shortuuid.ShortUUID().uuid())
    #
    # print(len(shortuuid.ShortUUID().uuid()))
    #
    # # print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    # # print(datetime.datetime.now().strftime('%y%m%d%H%M%S%f'))
    # # print(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    # print('{}{}'.format(datetime.datetime.now().strftime('%y%m%d%H%M%S'), random.randint(0, 99)))
    # # print(len('{}{}'.format(datetime.datetime.now().strftime('%y%m%d%H%M%S'), random.randint(0, 99))))
    #
    # default = models.short_uuid
    # print(default() if callable(default) else default)

    # db.create_all()

    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)

    t1 = Test(time=None)

    u2 = User(username='test2', register_time=None)
    u2.set_password('123')
    print(u2.register_time)
    db.session.add(u2)
    db.session.commit()
    print(u2.register_time)



