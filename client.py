import requests
from os import getenv

def send_data(value, auth_key):
    auth_token = auth_key
    url = "https://mybrillianthome.pl/api/reading/"
    data = {
        "value": value
    }
    header = {
        "Authorization": f"Token {auth_token}"
    }
    r = requests.post(url, json=data, headers=header, verify=False)
    print(r.text)

if __name__=='__main__':
    send_data(22, 'some-key')
    