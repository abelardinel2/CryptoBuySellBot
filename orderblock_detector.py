import requests
import pandas as pd
from datetime import datetime

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

    # Convert to weekly OHLC
    ohlc = df["price"].resample("W").ohlc().dropna()
    ohlc = ohlc.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close"})
    return ohlc

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

# Example usage:
btc_weekly = fetch_weekly_candles_from_coingecko("bitcoin")
btc_orderblock = detect_orderblock(btc_weekly)
print(f"BTC Orderblock Zone: {btc_orderblock['zone']} (From week of {btc_orderblock['date']})")