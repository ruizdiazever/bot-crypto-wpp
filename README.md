# Bot
This script automatically sends a message via Whatsapp Web when the price of BTC or ETH is at a set maximum or minimum. 

## Requirements 📝
- Python 3
- Coinbase API
- Browser
- Linux
- Whatsapp web


## Steps for your enviroment and the Script 👾
It is recommended that you use a virtual environment to install the necessary packages in it, this is done with the [virtualenv](https://pypi.org/project/virtualenv/) package, if you have doubts go to its documentation to learn how to use it, steps:
```bash
$ pip install virtualenv           # Install virtualenv
$ virtualenv coin                  # Make the coin enviroment
$ source coin/bin/activate         # Acivate the enviroment
```

In the project folder ```/coins``` install the required packages and run the program:
```
$ pip install -r requirements.txt
$ python coins.py
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
