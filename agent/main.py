import os, requests
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
r = requests.post(url, data={"chat_id": CHAT_ID, "text": "✅ MyLegalBot finally live! Mothi bhai, ab CHAT_ID sahi ho gaya."})
print(r.text)
