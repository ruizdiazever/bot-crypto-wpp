import time, webbrowser, subprocess
from coinbase.wallet.client import Client
import pyautogui


class Coin:
    def __init__(self, API_KEY, API_SECRET, PHONE, COIN, BROWSER, MAX, MIN):
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET
        self.PHONE = PHONE
        self.COIN = COIN
        self.BROWSER = BROWSER
        self.MAX = MAX
        self.MIN = MIN

    def path(self):
        with open(self.API_KEY) as f:
            self.API_KEY = f.read().strip()
        with open(self.API_SECRET) as f:
            self.API_SECRET = f.read().strip()
        with open(self.PHONE) as f:
            self.PHONE = f.read().strip()

    def price(self):
        client = Client(self.API_KEY, self.API_SECRET, api_version='YYYY-MM-DD')
        price = client.get_buy_price(currency_pair = self.COIN)
        price = float(price['amount'])
        return price
    
    def operation(self):
        i = 1
        self.lines = '------------'
        while(True):
            time.sleep(300)
            date = time.strftime("%d %b %Y %H:%M:%S")
            print(f'''{self.lines} {date} | MAX = {self.MAX} | MIN = {self.MIN} {self.lines}\n
                    ({i}) {self.COIN} --> {self.price()}\n\n''')
            i+=1

            if self.price() >= self.MAX or self.price() <= self.MIN:
                message = (f'Hey wake up, the price of {self.COIN} is {self.price()}')
                url = f'https://web.whatsapp.com/send?phone={self.PHONE}&text&app_absent=0'
                webbrowser.open(url, new=2, autoraise=True)
                f = message
                time.sleep(20)
                for word in f:
                    pyautogui.typewrite(word)
                pyautogui.press('enter')
                time.sleep(2)
                proc = subprocess.Popen(['pkill', self.BROWSER])


LINUX_API_KEY = '/home/ever/Dropbox/dev/keys/coinbase_api_key.txt'
LINUX_API_SECRET = '/home/ever/Dropbox/dev/keys/coinbase_api_secret.txt'
LINUX_PHONE = '/home/ever/Dropbox/dev/keys/phone_script_coin.txt'
RASPBERRY_API_KEY = '/home/pi/Desktop/Projects/keys/coinbase_api_key.txt'
RASPBERRY_API_SECRET = '/home/pi/Desktop/Projects/keys/coinbase_api_secret.txt'
RASPBERRY_PHONE = '/home/pi/Desktop/Projects/keys/phone_script_coin.txt'
ETH = 'ETH-EUR'
AMP = 'AMP-EUR'
ADA = 'ADA-EUR'
BROWSER = 'firefox'
MAX = 3
MIN = 1

t = Coin(LINUX_API_KEY, LINUX_API_SECRET, LINUX_PHONE, ADA, BROWSER, MAX, MIN)

t.path()
t.price()
t.operation()