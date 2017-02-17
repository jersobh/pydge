#!/usr/bin/env python
# encoding: utf-8
"""
router.py
"""
from views import render

def routes(app):
    app.router.add_get('/', render.index)
    app.router.add_get('/hey/', render.hey)
