#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import core.conf
import asyncio
from aiohttp import web
from core.router import routes

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
routes(app)
web.run_app(app, host='0.0.0.0', port=80)