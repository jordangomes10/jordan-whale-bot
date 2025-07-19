
import os
import time
import requests
from datetime import datetime, timedelta
from pytz import timezone

TOKEN = 'AAGWanBW5Rkstc96br_cN8bcJRTOdzD-Kww'
CHAT_ID = '@jordangomes10'
MIN_VALUE = 400000  # USD
TZ = timezone('America/Rio_branco')

def send_alert(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, data=data)
    except:
        pass

def check_fake_whale_alert():
    now = datetime.now(TZ)
    message = f'🐋 ALERTA DE WHALE\nToken: MEME\nValor: $450.000\nData: {now.strftime("%Y-%m-%d %H:%M:%S")} (Rio Branco)'
    send_alert(message)

if __name__ == "__main__":
    while True:
        check_fake_whale_alert()
        time.sleep(3600)  # a cada 1 hora simula alerta
