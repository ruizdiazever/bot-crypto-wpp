import time, webbrowser, subprocess
from coinbase.wallet.client import Client
import pyautogui


class Coin:
    def __init__(self, api_key, api_secret, phone_number, coin):
        self.api_key = api_key
        self.api_secret = api_secret
        self.phone_number = phone_number
        self.coin = coin

    def path(self):
        with open(self.api_key) as f:
            self.api_key = f.read().strip()
        with open(self.api_secret) as f:
            self.api_secret = f.read().strip()
        with open(self.phone_number) as f:
            self.phone_number = f.read().strip()

    def price(self):
        client = Client(self.api_key, self.api_secret, api_version='YYYY-MM-DD')
        price = client.get_buy_price(currency_pair = self.coin)
        price = price['amount']
        price = float(price)
        return price
    
    def operation(self):
        i = 1
        while(True):
            time.sleep(2)
            print(f'------------ {time.strftime("%d %b %Y %H:%M:%S")} ------------ \n({i}) {self.coin} --> {self.price()}\n')
            i+=1

            high = 1600
            print('Cambia? ', high)

            if self.price() >= high:

                # Message to send
                message = (f'##### HIGH, target {high} exceeded! ##### \nETH price is EUR {self.price()}')

                # New goal

                # Open navigator
                url = f'https://web.whatsapp.com/send?phone={self.phone_number}&text&app_absent=0'
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
                proc = subprocess.Popen(['pkill', 'chrome'])

            elif self.price() <= 1700:
                pass


api_key = '/home/ever/Dropbox/dev/keys/coinbase_api_key.txt'
api_secret = '/home/ever/Dropbox/dev/keys/coinbase_api_secret.txt'
phone = '/home/ever/Dropbox/dev/keys/phone_script_coin.txt'
eth = 'ETH-EUR'

t = Coin(api_key, api_secret, phone, eth)
t.path()
t.price()
t.operation()