# main.py – Daily Macro Zone Alert Bot (Reclaim Ladder Strategy)
import requests
from datetime import datetime

# === CONFIG ===
BOT_TOKEN = "7966331696:AAGAAvwtWAjYJsVO2LBNBVeQ3WHIbqexSMI"
CHAT_ID = "6652085600"  # Your personal Telegram chat ID

# === DYNAMIC DATE ===
today = datetime.now().strftime("%B %d, %Y")

# === ALERT MESSAGE ===
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

# === SEND ALERT ===
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {"chat_id": CHAT_ID, "text": message}

response = requests.get(url, params=params)
if response.status_code == 200:
    print("✅ Telegram alert sent successfully.")
else:
    print("❌ Failed to send alert:", response.text)