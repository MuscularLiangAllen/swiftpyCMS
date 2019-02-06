# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint(
    name='article',
    import_name=__name__
)


from app.article import routes