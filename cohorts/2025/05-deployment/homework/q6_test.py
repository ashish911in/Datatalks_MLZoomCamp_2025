"""
import requests
from time import sleep

# Use the Lambda RIE path if /predict doesn't work
url = "http://localhost:9696/predict"

client = {"job": "management", "duration": 400, "poutcome": "success"}

print("Starting load test... Press Ctrl+C to stop.")

while True:
    try:
        sleep(0.1)
        response = requests.post(url, json=client, timeout=1)
        print(response.json())
    except Exception as e:
        print(f"Error connecting to service: {e}")
"""

from urllib import response
import requests
import threading
from time import sleep
url = "http://localhost:9696/predict"

client = {"job": "management", "duration": 400, "poutcome": "success"}

def send_requests():
    while True:
        try:
            # No sleep here - maximum speed!
            response = requests.post(url, json=client, timeout=1)
            print(response.json())
        except Exception as e:
            print(f"Error connecting to service: {e}")

print("Launching 10 parallel workers to stress the CPU...")
for i in range(10):
    threading.Thread(target=send_requests, daemon=True).start()

# Keep the main thread alive
while True:
    sleep(1)