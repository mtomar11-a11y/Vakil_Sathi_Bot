import requests, os
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = "1755484304"  # direct daal diya

print(f"Using CHAT_ID: {CHAT_ID}")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
r = requests.post(url, data={"chat_id": CHAT_ID, "text": "✅ Fix ho gaya Mothi bhai! Bot live hai."})
print(r.text)
