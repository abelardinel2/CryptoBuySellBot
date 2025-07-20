import requests

bot_token = "7966331696:AAGAAvwtWAjYJsVO2LBNBVeQ3WHIbqexSMI"
chat_id = "6652085600"

message = (
    "📊 Daily Swing Alert – July 20, 2025\n"
    "🧭 Strategy: Reclaim Ladder\n\n"
    "🔹 BTCUSD\n📍 Zone: $117,000–$114,000\n🎯 Action: Limit Buy\n📝 Notes: Weekly orderblock – enter only after trap & reclaim\n\n"
    "🔹 ETHUSD\n📍 Zone: $2,720–$2,600\n🎯 Action: Limit Buy\n📝 Notes: Weekly demand zone – watch for reclaim after fakeout\n\n"
    "🔹 XRPUSD\n📍 Zone: $0.42–$0.40\n🎯 Action: Limit Buy\n📝 Notes: Reclaim zone below Y.Open – trap confirmation required\n\n"
    "🔹 SUIUSD\n📍 Zone: $0.68–$0.62\n🎯 Action: Limit Buy\n📝 Notes: Orderblock tested – wait for reclaim with RSI signal\n\n"
    "🔹 KASUSD\n📍 Zone: $0.129–$0.124\n🎯 Action: Limit Buy\n📝 Notes: Weekly support zone – entry on trap + reclaim only\n\n"
    "🔹 SOLUSDT\n📍 Zone: $124–$120\n🎯 Action: Limit Buy\n📝 Notes: Weekly orderblock – trap confirmation needed\n\n"
    "🔹 XLMUSDT\n📍 Zone: $0.075–$0.080\n🎯 Action: Limit Buy\n📝 Notes: Weekly OB zone – only enter on reclaim"
)

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
params = {"chat_id": chat_id, "text": message}
requests.get(url, params=params)