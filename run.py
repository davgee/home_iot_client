import client
from time import sleep

if __name__=='__main__':
    while True:
        your_key = "some_key"
        your_data = 22
        client.send_data(your_data, your_key)
        sleep(60)
        