#!/usr/bin/env python
# encoding: utf-8

import subprocess
cmdping = "python -m pwiz -e postgresql charles_blog > blog_models.py"
p = subprocess.Popen(cmdping, shell=True, stderr=subprocess.PIPE)


