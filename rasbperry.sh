#!/usr/bin/env bash
sudo apt update
sudo apt install python3 idle3
echo "alias python=/usr/bin/python3" >> ~/.bashrc
source ~/.bashrc
python3 -m venv venv
source venv/bin/activate 
python3 -m pip install -U -r requirements.txt
python3 -m pip install --upgrade pip
python3 bot.py