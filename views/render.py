#!/usr/bin/env python
# encoding: utf-8
"""
render.py
"""
from aiohttp import web
from jinja2 import Template

async def index(request):
    return web.Response(text="Hello, world") #use the path to jinja2 template

async def hey(request):
    return web.Response(text="Hey you!") #use the path to jinja2 template
