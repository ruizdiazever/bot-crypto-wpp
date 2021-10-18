# Bot
This script automatically sends a message via Whatsapp Web when the price of BTC, ETH, ADA or others is at a set maximum or minimum. 

## Requirements 📝
- Python 3
- Coinbase API
- Firefox
- Linux
- Whatsapp web


## Run 👾
Only for GNU/Linux and Mac OS
```bash
sh run.sh                # Other Linux system 🐧
sh raspberry.sh          # Raspberry Pi OS 🍓
```

## Raspberry Pi OS manual configuration (without Bash Script) 🐧
```bash
sudo apt update                                   # Update OS packages
sudo apt install python3 idle3                    # Install Python 3 in OS
echo "alias python=/usr/bin/python3" >> ~/.bashrc # Python 3 config set as default
source ~/.bashrc
python3 -m venv venv                              # Make enviroment
source venv/bin/activate                          # Activate enviroment
python3 -m pip install -U -r requirements.txt     # Install requirements
python3 -m pip install --upgrade pip              # Upgrade pip
python3 bot.py                                    # Run bot
```
See more in about [Raspberry Pi OS](https://www.raspberrypi.org/software/)
