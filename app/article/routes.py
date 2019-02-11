# -*- coding: utf-8 -*-
import os

import shortuuid
from flask import render_template, request, flash, redirect, url_for, jsonify, make_response, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename

from app import db, Config
from app.article import bp
from app.forms import ArticleForm
from app.models import Article, Image

from PIL import Image as im


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        if Article.query.filter_by(title=article_form.title.data).first() is not None:
            flash('Same title already existed in the database')
        elif db.session.query(Article).filter_by(url=article_form.url.data).first() is not None:
            flash('Same URL already existed in the database')
        else:
            article = Article(title=article_form.title.data, intro=article_form.intro.data,
                              content=article_form.content.data,
                              url=article_form.url.data if article_form.url.data.strip() != '' else None)
            db.session.add(article)
            db.session.commit()
    return render_template('article/editor.html', article_form=article_form)


@bp.route('/test-json', methods=['GET'])
def test_json():
    return jsonify({'data': ['default_head.jpg', 'logo.png'], 'errno': 0})


@bp.route('/upload/img', methods=['POST'])
@login_required
def upload_img():
    upload_path = os.path.join(Config.FS_ROOT_DIR, Config.FS_ROOT_UPLOAD, Config.FS_ROOT_IMG_UPLOAD)
    abs_up_path = os.path.abspath(upload_path)
    if not os.path.exists(abs_up_path):
        os.makedirs(abs_up_path)
    resp_dict = {'errno': 0, 'data': []}
    try:
        files = request.files.to_dict()
        for filename, file in files.items():
            uuid_filename = '{}.{}'.format(shortuuid.uuid(), secure_filename(filename).rsplit('.')[-1])
            # compress the upload img
            compress2png(file, dst=os.path.join(abs_up_path, uuid_filename))
            resp_dict['data'].append('/article/img/%s' % uuid_filename.split('.')[0])
            img = Image(id=uuid_filename.split('.')[0], local_path=os.path.join(abs_up_path, uuid_filename))
            db.session.add(img)
            db.session.commit()
    except Exception as e:
        print(e)
        resp_dict['errno'] = 1

    return jsonify(resp_dict)


@bp.route('/img/<string:img_name>', methods=['GET'])
def get_img(img_name: str):
    img = Image.query.filter_by(id=img_name).first()
    pic_path = img.local_path if img else os.path.join(current_app.root_path, 'static/img/piclost.png')

    with open(pic_path, 'rb') as i:
        response = make_response(i.read())
        response.headers['Content-Type'] = 'image/%s' % (os.path.splitext(pic_path)[1])

    return response


def compress2png(src, dst=None, size=(480, 480)):
    '''
    :param src: a string path of a file object
    :param dst:
    :param size: default (480, 480)
    :return:
    '''

    if dst is None and type(src) != str:
        raise IOError('src must be a str path if dst=None')
    i = im.open(src)
    size = size if i.width >= 480 else (i.width, i.height)
    i.thumbnail(size, im.ANTIALIAS)
    dst = src if dst is None else dst
    # i.save('%s.png' % os.path.splitext(dst)[0])
    i.save(dst)
