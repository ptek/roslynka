import requests
import os

PUSHOVER_APP_TOKEN = os.environ.get('PUSHOVER_APP_TOKEN')
PUSHOVER_USER_KEY = os.environ.get('PUSHOVER_USER_KEY')

def powiadom(text: str):
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
    "token": PUSHOVER_APP_TOKEN,
    "user": PUSHOVER_USER_KEY,
    "message": text,
    })
    if r.status_code != 200:
        print("Nie udało się wysłać powiadomienia!")
        print(r.text)
