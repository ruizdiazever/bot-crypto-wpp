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
```
sh run.sh                # Other Linux system 🐧
sh raspberry.sh          # Raspberry Pi OS 🍓
```

## Raspberry Pi OS configuration 🐧
Install Python 3 in [Raspberry Pi OS](https://www.raspberrypi.org/software/)
```
$ sudo apt update
$ sudo apt install python3 idle3
```
Python 3 configuration set as default in Raspberry Pi OS
```
$ echo "alias python=/usr/bin/python3.7" >> ~/.bashrc
$ source ~/.bashrc
```
Install requirements in Raspberry Pi OS and run
```
$ sudo python3 pip install -r requirements
$ python3 coins.py
```
