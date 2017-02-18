#!/usr/bin/env python
# encoding: utf-8
"""
router.py
"""
from controllers import index

def routes(app):
    app.router.add_static('/static/',
                      path=str('views/static'),
                      name='static')
    app.router.add_get('/', index.main)
    #app.router.add_get('/hey/', render.hey)
