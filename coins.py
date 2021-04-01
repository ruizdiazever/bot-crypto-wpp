import time,  webbrowser, subprocess
from coinbase.wallet.client import Client
import pyautogui


# KEYS
with open('/home/ever/Dropbox/dev/keys/coinbase_api_key.txt') as f:
    api_key = f.read().strip()
with open('/home/ever/Dropbox/dev/keys/coinbase_api_secret.txt') as f:
    api_secret = f.read().strip()
with open('/home/ever/Dropbox/dev/keys/phone_script_coin.txt') as f:
    phone = f.read().strip()


while(True):

    # Time loop
    time.sleep(5)
    
    # API
    client = Client(api_key, api_secret, api_version='YYYY-MM-DD')
    price_btc = client.get_buy_price(currency_pair = 'BTC-EUR')
    price_eth = client.get_buy_price(currency_pair = 'ETH-EUR')
    price_btc = price_btc['amount']
    price_eth = price_eth['amount']
    price_btc = float(price_btc)
    price_eth = float(price_eth)
    print(f'------------ {time.strftime("%d %b %Y %H:%M:%S")} ------------ \nETH € {price_eth} \nBTC € {price_btc}')


    if price_btc >= 55000 or price_eth >= 1722:

        # Message to send
        message = (f'######## SUPER HIGH ######## \nBTC price is EUR {price_btc} \nETH price is EUR {price_eth}')

        # Open navigator
        url = f'https://web.whatsapp.com/send?phone={phone}&text&app_absent=0'
        webbrowser.open(url, new=2, autoraise=True)
        f = message

        # Waiting time for whatsapp to be ready
        time.sleep(20)

        # Write message
        for word in f:
            pyautogui.typewrite(word)
        pyautogui.press('enter')

        # Kill Chrome
        time.sleep(2)
        proc = subprocess.Popen(['pkill', 'chrome'])

    elif price_btc <= 46300 or price_eth <= 1522:
        message = (f'######## SUPER LOW ######## \nBTC price is EUR {price_btc} \nETH price is EUR {price_eth}')
        url = f'https://web.whatsapp.com/send?phone={phone}&text&app_absent=0'

        webbrowser.open(url, new=2, autoraise=True)
        f = message

        time.sleep(20)

        for word in f:
            pyautogui.typewrite(word)
        pyautogui.press('enter')

        time.sleep(2)

        proc = subprocess.Popen(['pkill', 'chrome'])