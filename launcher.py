# -*- coding: utf-8 -*-

# @Time    : 2019/1/31 9:58 PM
import os

from app import create_app, Config

__author__ = 'Allen LIANG'

if __name__ == '__main__':
    app = create_app(Config)
    try:
        # img upload directories
        upload_path = os.path.join(Config.FS_ROOT_DIR, Config.FS_ROOT_UPLOAD, Config.FS_ROOT_IMG_UPLOAD)
        abs_up_path = os.path.abspath(upload_path)
        if not os.path.exists(abs_up_path):
            os.makedirs(abs_up_path)
        print('Sys FS [{}] already existed...'.format(abs_up_path))
    except PermissionError as e:
        print('Create [{}] failed : [{}]'.format(abs_up_path, e))

    app.run(debug=True, port=8080)
