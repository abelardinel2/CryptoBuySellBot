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

    # Resample daily data into weekly OHLC
    ohlc = df["price"].resample("W").ohlc().dropna()
    ohlc = ohlc.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close"})
    return ohlc

# Example: BTC
btc_weekly = fetch_weekly_candles_from_coingecko("bitcoin")
print(btc_weekly.tail(5))
