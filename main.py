# main.py – BuySellZonesCrypyoBot (Reclaim Ladder Strategy Alerts)
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# === Load credentials from .env ===
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# === Format today's date ===
today = datetime.now().strftime("%B %d, %Y")

# === Prepare daily macro alert message ===
message = f"""📊 Daily Swing Alert – {today}
🧭 Strategy: Reclaim Ladder

🔹 BTCUSD
📍 Zone: $117,000–$114,000
🎯 Action: Limit Buy
📝 Notes: Weekly orderblock – enter only after trap & reclaim

🔹 ETHUSD
📍 Zone: $2,720–$2,600
🎯 Action: Limit Buy
📝 Notes: Weekly demand zone – watch for reclaim after fakeout

🔹 XRPUSD
📍 Zone: $0.42–$0.40
🎯 Action: Limit Buy
📝 Notes: Reclaim zone below Y.Open – trap confirmation required

🔹 SUIUSD
📍 Zone: $0.68–$0.62
🎯 Action: Limit Buy
📝 Notes: Orderblock tested – wait for reclaim with RSI signal

🔹 KASUSD
📍 Zone: $0.129–$0.124
🎯 Action: Limit Buy
📝 Notes: Weekly support zone – entry on trap + reclaim only

🔹 SOLUSDT
📍 Zone: $124–$120
🎯 Action: Limit Buy
📝 Notes: Weekly orderblock – trap confirmation needed

🔹 XLMUSDT
📍 Zone: $0.075–$0.080
🎯 Action: Limit Buy
📝 Notes: Weekly OB zone – only enter on reclaim
"""

# === Send alert to Telegram ===
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {"chat_id": CHAT_ID, "text": message}

response = requests.get(url, params=params)
if response.status_code == 200:
    print("✅ Telegram alert sent successfully.")
else:
    print(f"❌ Failed to send alert: {response.text}")