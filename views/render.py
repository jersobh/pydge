#!/usr/bin/env python
# encoding: utf-8
"""
render.py
"""
from aiohttp import web
import aiohttp_jinja2
import jinja2
from jinja2 import Template

async def view(request, template, context):
    response = aiohttp_jinja2.render_template(template,
                                              request,
                                              context)
    response.headers['Content-Language'] = 'en'
    return response

async def json(data, status, headers = None):
    response = web.json_response(data, status=status, headers=None, content_type='application/json')
    return response
