import pandas as pd

def moving_average_strategy(df):
    df["short_ma"] = df["close"].rolling(5).mean()
    df["long_ma"] = df["close"].rolling(20).mean()

    df["signal"] = df["short_ma"] > df["long_ma"]

    return df
