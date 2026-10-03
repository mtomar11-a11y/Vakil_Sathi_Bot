import os
import requests
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
print(f"CHAT_ID from secret: {CHAT_ID}")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": "Namaste! Vakil Sathi Bot Live ho gaya hai ✅"}
r = requests.post(url, data=data)
print(f"TELEGRAM API RESPONSE: {r.text}")
