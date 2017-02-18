#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import core.conf
import asyncio
import jinja2
import aiohttp_jinja2
from aiohttp import web
from core.router import routes

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
routes(app)
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('views/templates'))
web.run_app(app, host='0.0.0.0', port=8080)
