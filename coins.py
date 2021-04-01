import time, webbrowser, subprocess
from coinbase.wallet.client import Client
import pyautogui

fedora_api_key = '/home/ever/Dropbox/dev/keys/coinbase_api_key.txt'
fedora_api_secret = '/home/ever/Dropbox/dev/keys/coinbase_api_secret.txt'
fedora_phone = '/home/ever/Dropbox/dev/keys/phone_script_coin.txt'

raspberry_api_key = '/home/pi/Desktop/Projects/keys/coinbase_api_key.txt'
raspberry_api_secret = '/home/pi/Desktop/Projects/keys/coinbase_api_secret.txt'
raspberry_phone = '/home/pi/Desktop/Projects/keys/phone_script_coin.txt'

# KEYS, here your personal configuration
with open(raspberry_api_key) as f:
    api_key = f.read().strip()
with open(raspberry_api_secret) as f:
    api_secret = f.read().strip()
with open(raspberry_phone) as f:
    phone = f.read().strip()
    
client = Client(api_key, api_secret, api_version='YYYY-MM-DD')

# Loop
while(True):
    # API
    time.sleep(2)
    
    price_btc = client.get_buy_price(currency_pair = 'BTC-EUR')
    price_eth = client.get_buy_price(currency_pair = 'ETH-EUR')
    price_btc = price_btc['amount']
    price_eth = price_eth['amount']
    price_btc = float(price_btc)
    price_eth = float(price_eth)
    print(f'------------ {time.strftime("%d %b %Y %H:%M:%S")} ------------ \nETH € {price_eth} \nBTC € {price_btc}')

    # HIGH PRICE
    if price_btc >= 40000 or price_eth >= 1722:

        # Message to send
        message = (f'######## SUPER HIGH ######## \nBTC price is EUR {price_btc} \nETH price is EUR {price_eth}')

        # Open navigator
        url = f'https://web.whatsapp.com/send?phone={phone}&text&app_absent=0'
        webbrowser.open(url, new=2, autoraise=True)
        f = message

        # Waiting time for whatsapp to be ready
        time.sleep(8)

        # Write message
        for word in f:
            pyautogui.typewrite(word)
        pyautogui.press('enter')

        time.sleep(2)
        
        # Here should be your default browser command for kill the browser
        proc = subprocess.Popen(['pkill', 'chromium'])

    # LOW PRICE
    elif price_btc <= 46300 or price_eth <= 1522:
        message = (f'######## SUPER LOW ######## \nBTC price is EUR {price_btc} \nETH price is EUR {price_eth}')
        url = f'https://web.whatsapp.com/send?phone={phone}&text&app_absent=0'

        webbrowser.open(url, new=2, autoraise=True)
        f = message

        time.sleep(10)

        for word in f:
            pyautogui.typewrite(word)
        pyautogui.press('enter')

        time.sleep(2)
        proc = subprocess.Popen(['pkill', 'chromium'])
        