#!/bin/bash
virtualenv pydge_env
pip -q install -r requirements.txt
python server.py
