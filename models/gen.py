#!/usr/bin/env python
# encoding: utf-8
"""
gen.py
"""
import subprocess

if GENERATE_MODELS:
    cmdping = "python -m pwiz -e postgresql %d > %d.py" % DB
    p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
