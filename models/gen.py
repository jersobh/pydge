#!/usr/bin/env python
# encoding: utf-8
"""
gen.py
"""
import subprocess
from core.conf import *

if GENERATE_MODELS:
    cmdping = "python -m pwiz -u %s -e postgresql %s > models/models.py" % (DB_USER, DB)
    p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
