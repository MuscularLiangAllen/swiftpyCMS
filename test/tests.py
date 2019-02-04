# -*- coding: utf-8 -*-
import datetime
import uuid

import time

from app.models import User

if __name__ == '__main__':
    print(len(uuid.uuid4().hex))
    uuid4 = uuid.uuid4()
    print(uuid4)
    print(uuid4.hex)
    print(str(uuid4).replace('-', ''))
    print(time.time())
    print(datetime.datetime.timestamp(datetime.datetime.now()))
    print('%015d%s'%((time.time()*1000), uuid4.hex))
    print(len('%015d%s'%((time.time()*1000), uuid4.hex)))

    u = User()
    print(type(u))