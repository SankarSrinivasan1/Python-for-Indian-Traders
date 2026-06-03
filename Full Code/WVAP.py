from kiteconnect import KiteConnect
import pandas as pd
from datetime import datetime, timedelta

# =====================================
# CONFIGURATION
# =====================================

API_KEY = "YOUR_API_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

SYMBOL = "RELIANCE"
EXCHANGE = "NSE"

# Example instrument token for RELIANCE
# Replace with latest token from Kite instruments dump
INSTRUMENT_TOKEN = 738561

INTERVAL = "5minute"

# =====================================
# KITE LOGIN
# =====================================

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# =====================================
# FETCH HISTORICAL DATA
# =====================================

def fetch_data():

    to_date = datetime.now()
    from_date = to_date - timedelta(days=5)

    candles = kite.historical_data(
        instrument_token=INSTRUMENT_TOKEN,
        from_date=from_date,
        to_date=to_date,
        interval=INTERVAL
    )

    df = pd.DataFrame(candles)

    return df


# =====================================
# VWAP CALCULATION
# =====================================

def calculate_vwap(df):

    typical_price = (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3

    tp_volume = typical_price * df["volume"]

    cumulative_tp_volume = tp_volume.cumsum()

    cumulative_volume = df["volume"].cumsum()

    df["vwap"] = cumulative_tp_volume / cumulative_volume

    return df


# =====================================
# SIGNAL GENERATION
# =====================================

def generate_signal(df):

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    latest_close = latest["close"]
    latest_vwap = latest["vwap"]

    previous_close = previous["close"]
    previous_vwap = previous["vwap"]

    buy_signal = (
        previous_close < previous_vwap
        and
        latest_close > latest_vwap
    )

    sell_signal = (
        previous_close > previous_vwap
        and
        latest_close < latest_vwap
    )

    if buy_signal:
        return "BUY"

    elif sell_signal:
        return "SELL"

    else:
        return "HOLD"


# =====================================
# DISPLAY RESULT
# =====================================

def print_summary(df, signal):

    latest = df.iloc[-1]

    print("\n" + "=" * 50)

    print("SYMBOL :", SYMBOL)

    print("TIME   :", latest["date"])

    print("CLOSE  :", round(latest["close"], 2))

    print("VWAP   :", round(latest["vwap"], 2))

    print("SIGNAL :", signal)

    print("=" * 50)


# =====================================
# MAIN
# =====================================

def main():

    df = fetch_data()

    if len(df) < 2:
        print("Not enough data")
        return

    df = calculate_vwap(df)

    signal = generate_signal(df)

    print_summary(df, signal)


if __name__ == "__main__":
    main()
