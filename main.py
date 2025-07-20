# main.py – BuySellZonesCrypyoBot with live OB detection from CoinGecko
import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# === Load Telegram credentials from .env ===
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# === Fetch Weekly Candles from CoinGecko ===
def fetch_weekly_candles_from_coingecko(coin_id="bitcoin", vs_currency="usd", days=90):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": vs_currency,
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)
    ohlc = df["price"].resample("W").ohlc().dropna()
    ohlc = ohlc.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close"})
    return ohlc

# === Detect Orderblock (last red candle before breakout) ===
def detect_orderblock(weekly_df):
    for i in range(len(weekly_df) - 2, 1, -1):
        current = weekly_df.iloc[i]
        next_candle = weekly_df.iloc[i + 1]
        if current["Close"] < current["Open"]:
            if next_candle["Close"] > next_candle["Open"] and next_candle["Close"] > current["High"]:
                return {
                    "zone": f"${round(current['Low'], 2)} – ${round(current['High'], 2)}",
                    "date": weekly_df.index[i].strftime("%Y-%m-%d")
                }
    return {"zone": "Not Found", "date": "N/A"}

# === Build Telegram message ===
today = datetime.now().strftime("%B %d, %Y")
btc_ohlc = fetch_weekly_candles_from_coingecko("bitcoin")
btc_ob = detect_orderblock(btc_ohlc)

message = f"""📊 Daily Swing Alert – {today}
🧭 Strategy: Reclaim Ladder (Auto OB Zones)

🔹 BTCUSD
📍 Orderblock Zone: {btc_ob['zone']}
🗓️ Detected from week of: {btc_ob['date']}
🎯 Action: Limit Buy (after trap + reclaim)
"""

# === Send Telegram message ===
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {"chat_id": CHAT_ID, "text": message}

response = requests.get(url, params=params)
if response.status_code == 200:
    print("✅ Telegram alert sent successfully.")
else:
    print(f"❌ Failed to send alert: {response.text}")