#!/usr/bin/env bash
sudo apt update                                   # Update OS packages
sudo apt install python3 idle3                    # Install Python 3 in OS
echo "alias python=/usr/bin/python3" >> ~/.bashrc # Python 3 configuration set as default
source ~/.bashrc
python3 -m venv venv                              # Make enviroment
source venv/bin/activate                          # Activate enviroment
python3 -m pip install -U -r requirements.txt     # Install requirements
python3 -m pip install --upgrade pip              # Upgrade pip
python3 bot.py                                    # Run bot