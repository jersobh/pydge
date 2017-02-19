#!/usr/bin/env python
# encoding: utf-8
"""
gen.py
"""
import subprocess
from core.conf import *

if GENERATE_MODELS:
    cmdping = "python -m pwiz -u %s -P %s -p %s -e %s %s > models/models.py" % (DB_USER, DB_PASS, DB_PORT, DB_TYPE, DB)
    p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
