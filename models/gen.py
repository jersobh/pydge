#!/usr/bin/env python
# encoding: utf-8
"""
gen.py
"""
import subprocess
from core.conf import *

if GENERATE_MODELS:
    if DB_PASS:
        cmdping = "python -m pwiz -H %s -u %s -P %s -p %s -e %s %s > models/models.py" % (DB_HOST, DB_USER, DB_PASS, DB_PORT, DB_TYPE, DB)
    else:
        cmdping = "python -m pwiz -H %s -u %s -p %s -e %s %s > models/models.py" % (DB_HOST, DB_USER, DB_PORT, DB_TYPE, DB)
        
        p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
