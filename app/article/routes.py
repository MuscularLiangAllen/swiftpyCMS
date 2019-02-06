# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for

from app import db
from app.article import bp
from app.forms import ArticleForm
from app.models import Article


@bp.route('/add', methods=['GET', 'POST'])
def add_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article = Article.query.filter_by(title=article_form.title.data).first()
        if article is not None:
            flash('Same title already existed in the database')
            return render_template('article/editor.html', article_form=article_form)
        article = db.session.query(Article).filter_by(url=article_form.url.data).first()
        if article is not None:
            flash('Same URL already existed in the database')
            return render_template('article/editor.html', article_form=article_form)
        article = Article(title=article_form.title.data, intro=article_form.intro.data,
                          content=article_form.content.data,
                          url=article_form.url.data if article_form.url.data.strip() != '' else None)
        db.session.add(article)
        db.session.commit()
    return render_template('article/editor.html', article_form=article_form)