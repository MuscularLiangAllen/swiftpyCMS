# -*- coding: utf-8 -*-
import datetime
import random
import uuid

import time

from app import db, models
from app.models import User

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
    from app.models import User

    u1 = User(username='kingroot', email='liangtee@126.com')
    u1.set_password('kingroot')
    db.session.add(u1)
    db.session.commit()
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



