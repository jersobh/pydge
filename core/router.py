#!/usr/bin/env python
# encoding: utf-8
from views.templates import *
from views.static import *

def routes(app):
    app.router.add_get('/', index)