#!/usr/bin/env python
# encoding: utf-8
"""
render.py
"""
from aiohttp import web
import aiohttp_jinja2
import jinja2
from jinja2 import Template

async def index(request):
    context = {'name': 'Pydge Framework', 'github': 'https://github.com/jersobh/pydge'}
    response = aiohttp_jinja2.render_template('index.jinja2',
                                              request,
                                              context)
    response.headers['Content-Language'] = 'en'
    return response

async def hey(request):
    return web.Response(text="Hey you!") #use the path to jinja2 template

