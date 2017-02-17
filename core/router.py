#!/usr/bin/env python
# encoding: utf-8
from ...views import render

def routes(app):
    app.router.add_get('/', index)