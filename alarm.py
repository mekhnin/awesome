import psutil
import requests
from time import sleep

limit = 1e9
url = 'http:/localhost/alarm'

while True:
    current = psutil.virtual_memory().available
    if current < limit:
        requests.post(url, json = {'available': current})    
    sleep(60)

