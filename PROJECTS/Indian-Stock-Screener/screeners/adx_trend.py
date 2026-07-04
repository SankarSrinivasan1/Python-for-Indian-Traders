"""
ADX Trend Screener

Condition

ADX > Threshold

Default Threshold = 25
"""

import pandas as pd
import pandas_ta as ta

DEFAULT_LENGTH = 14
DEFAULT_THRESHOLD = 25


def calculate_adx(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH
):

    adx = ta.adx(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=length
    )

    return adx


def screen(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    threshold: float = DEFAULT_THRESHOLD
):

    if len(df) < length + 10:
        return False

    df = df.copy()

    adx = calculate_adx(df, length)

    latest = adx.iloc[:, 0].iloc[-1]

    if pd.isna(latest):
        return False

    return latest > threshold


def latest_value(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH
):

    adx = calculate_adx(df, length)

    value = adx.iloc[:, 0].iloc[-1]

    if pd.isna(value):
        return None

    return round(float(value), 2)


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    print("ADX :", latest_value(df))
    print("Strong Trend :", screen(df))
