#!/usr/bin/env python
# encoding: utf-8
"""
controller.py
"""
from views import render
from models import db
from models import gen

def index(request):
    context = {'name': 'Pydge Framework', 'github': 'https://github.com/jersobh/pydge'}
    template = 'index.jinja2'
    return render.view(request, template, context)
