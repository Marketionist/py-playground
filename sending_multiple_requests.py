# python3 send_tons_of_requests.py

import requests
import threading

url = 'https://www.google.com'
data = {}

def send_a_ton (url, data):
    while True:
        # response = requests.post(url, data=data).text
        response = requests.get(url, data=data).text
        print(response)

threads = []

# Fill the threads array with threads
for i in range(50):
    t = threading.Thread(target=send_a_ton, args=[url, data])
    t.daemon = True
    threads.append(t)

# Start each of the threads
for i in range(50):
    threads[i].start()

# Join each of the threads
for i in range(50):
    threads[i].join()
