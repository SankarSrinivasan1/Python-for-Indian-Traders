from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta
import requests

# ==========================================
# CONFIGURATION
# ==========================================

API_KEY = "YOUR_API_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

INSTRUMENT_TOKEN = 738561      # Example RELIANCE
SYMBOL = "RELIANCE"

INTERVAL = "5minute"

# Telegram (Optional)

TELEGRAM_ENABLED = True

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# ==========================================
# KITE LOGIN
# ==========================================

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# ==========================================
# TELEGRAM ALERT
# ==========================================

def send_telegram(message):

    if not TELEGRAM_ENABLED:
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print("Telegram Error:", e)

# ==========================================
# FETCH DATA
# ==========================================

def fetch_data():

    end_date = datetime.now()
    start_date = end_date - timedelta(days=10)

    data = kite.historical_data(
        instrument_token=INSTRUMENT_TOKEN,
        from_date=start_date,
        to_date=end_date,
        interval=INTERVAL
    )

    return pd.DataFrame(data)

# ==========================================
# CALCULATE INDICATORS
# ==========================================

def calculate_indicators(df):

    typical_price = (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3

    df["vwap"] = (
        (typical_price * df["volume"]).cumsum()
        /
        df["volume"].cumsum()
    )

    df["ema20"] = df["close"].ewm(
        span=20,
        adjust=False
    ).mean()

    df["ema50"] = df["close"].ewm(
        span=50,
        adjust=False
    ).mean()

    df["avg_volume"] = (
        df["volume"]
        .rolling(20)
        .mean()
    )

    return df

# ==========================================
# SIGNAL ENGINE
# ==========================================

def generate_signal(df):

    latest = df.iloc[-1]

    close_price = latest["close"]
    vwap = latest["vwap"]

    ema20 = latest["ema20"]
    ema50 = latest["ema50"]

    volume = latest["volume"]
    avg_volume = latest["avg_volume"]

    bullish_trend = ema20 > ema50
    bearish_trend = ema20 < ema50

    strong_volume = volume > avg_volume

    buy_signal = (
        close_price > vwap
        and bullish_trend
        and strong_volume
    )

    sell_signal = (
        close_price < vwap
        and bearish_trend
        and strong_volume
    )

    if buy_signal:
        return "BUY"

    if sell_signal:
        return "SELL"

    return "HOLD"

# ==========================================
# SIGNAL REPORT
# ==========================================

def print_report(df, signal):

    latest = df.iloc[-1]

    print("\n")
    print("=" * 60)

    print("Symbol :", SYMBOL)
    print("Time   :", latest["date"])

    print("Close  :", round(latest["close"], 2))
    print("VWAP   :", round(latest["vwap"], 2))

    print("EMA20  :", round(latest["ema20"], 2))
    print("EMA50  :", round(latest["ema50"], 2))

    print("Volume :", int(latest["volume"]))

    print("Signal :", signal)

    print("=" * 60)

# ==========================================
# ALERT MESSAGE
# ==========================================

def create_message(df, signal):

    latest = df.iloc[-1]

    return f"""
VWAP SIGNAL

Symbol : {SYMBOL}
Signal : {signal}

Close : {latest['close']:.2f}
VWAP  : {latest['vwap']:.2f}

EMA20 : {latest['ema20']:.2f}
EMA50 : {latest['ema50']:.2f}

Time  : {latest['date']}
"""

# ==========================================
# MAIN
# ==========================================

def main():

    try:

        df = fetch_data()

        if len(df) < 60:
            print("Insufficient data")
            return

        df = calculate_indicators(df)

        signal = generate_signal(df)

        print_report(df, signal)

        if signal in ["BUY", "SELL"]:

            msg = create_message(df, signal)

            send_telegram(msg)

    except Exception as e:

        print("Error:", e)

# ==========================================

if __name__ == "__main__":
    main()
