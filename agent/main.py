import os, requests
TOKEN = os.getenv("TELEGRAM_TOKEN")
r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates")
print(r.text)
