import requests
import time

from flask import session

from main import app

def req(url):
    for i in range(1, 26):
        forma = {
            'email': str(f'{"Bot"}{i}@{"mail.ru"}'),
            'password': i,
        }
        response = requests.post(url, data=forma)
        print(response.status_code)

        if response.status_code == 429:
            time.sleep(60)
        if response.status_code == 200:
            return forma

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/login'
    req(url)

