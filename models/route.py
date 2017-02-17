#!/usr/bin/env python
# encoding: utf-8
from peewee import *
import json
import urllib2
from playhouse.postgres_ext import *

psql_db = PostgresqlDatabase( conf.DB, user='postgres')
db = PostgresqlExtDatabase(conf.DB)  
