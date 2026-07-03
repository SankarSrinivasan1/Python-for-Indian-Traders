"""
RSI Overbought Screener

Condition

RSI > Threshold

Default Threshold = 70
"""

import pandas as pd
import pandas_ta as ta

DEFAULT_LENGTH = 14
DEFAULT_THRESHOLD = 70


def calculate_rsi(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH
) -> pd.Series:
    """
    Calculate RSI.
    """
    return ta.rsi(df["Close"], length=length)


def screen(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    threshold: float = DEFAULT_THRESHOLD
) -> bool:
    """
    Returns True if RSI is above threshold.
    """

    if len(df) < length + 5:
        return False

    df = df.copy()

    df["RSI"] = calculate_rsi(df, length)

    latest = df["RSI"].iloc[-1]

    if pd.isna(latest):
        return False

    return latest > threshold


def latest_value(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH
):
    """
    Latest RSI value.
    """

    df = df.copy()

    df["RSI"] = calculate_rsi(df, length)

    value = df["RSI"].iloc[-1]

    if pd.isna(value):
        return None

    return round(float(value), 2)


if __name__ == "__main__":

    import yfinance as yf

    symbol = "RELIANCE.NS"

    df = yf.download(
        symbol,
        period="6mo",
        progress=False
    )

    print("Latest RSI :", latest_value(df))
    print("Overbought :", screen(df))
