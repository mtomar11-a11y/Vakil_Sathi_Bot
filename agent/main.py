import os
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "Namaste! Vakil Sathi Bot Live ho gaya hai ✅\nKal se aapke cases ke alerts yahi aayenge."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": message})

print("Message bhej diya")
