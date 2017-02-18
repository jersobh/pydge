#!/usr/bin/env python
# encoding: utf-8
"""
db.py
"""
import asyncio
import peewee
import logging
from peewee_async import Manager, PostgresqlDatabase
from core.conf import *

loop = asyncio.new_event_loop()
database = PostgresqlDatabase(DB)
objects = Manager(database, loop=loop)
