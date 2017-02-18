#!/usr/bin/env python
# encoding: utf-8
"""
controller.py
"""
from views import render
from models import db
from models import gen
from models import models

def index(request):
    context = {'name': 'Pydge Framework', 'github': 'https://github.com/jersobh/pydge'}
    template = 'index.jinja2'
    models.Users.create(username='Charlie') #my example has USERS table with username field)
    return render.view(request, template, context)
