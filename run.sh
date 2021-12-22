#!/usr/bin/env bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install -U -r requirements.txt
echo 'Successfully created environment. Wait 5 minutes.'
python3 bot.py