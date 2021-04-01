# Script
- This script automatically sends a message via Whatsapp Web when the price of BTC or ETH is at a set maximum or minimum. (EN)  
- Este script envia un mensaje automaticamente un mensaje por Whatsapp Web cuando el precio del BTC o ETH se encuenta en un maximo o minimo establecido. (ES)


### Requisitos 📝
- Linux
- Google Chrome
- API Key and Secret key from Coinbase with your Coinbase Account
- Python 3
- Virtual enviroment (recommended)
- Raspberry Pi to leave the script active (recommended)
- Phone number


### Steps for your enviroment
```bash
$ pip install virtualenv           # Install virtualenv
$ virtualenv coin                  # Make
$ source coin/bin/activate         # Acivate
```

- In the folder script
    ```
    $ pip install -r requirements.txt
    ```
- Run the script

### Personal notes
Install Python 3 in Raspberry Pi OS
```
$ sudo apt update
$ sudo apt install python3 idle3
```
Python 3 configuration
```
$ echo "alias python=/usr/bin/python3.7" >> ~/.bashrc
$ source ~/.bashrc
```
Install requirements in Raspberry Pi OS
```
$ sudo python3 pip install -r requirements
```

Run in Raspberry Pi OS
```
$ python3 coins.py
```