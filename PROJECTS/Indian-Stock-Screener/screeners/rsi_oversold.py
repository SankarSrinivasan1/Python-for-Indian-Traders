"""
RSI Oversold Screener

Condition

RSI < Threshold

Default Threshold = 30
"""

import pandas as pd
import pandas_ta as ta


DEFAULT_LENGTH = 14
DEFAULT_THRESHOLD = 30


def calculate_rsi(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH
) -> pd.Series:
    """
    Calculate RSI.

    Parameters
    ----------
    df : DataFrame
        OHLCV dataframe

    length : int
        RSI Period

    Returns
    -------
    Series
    """

    return ta.rsi(df["Close"], length=length)


def screen(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    threshold: float = DEFAULT_THRESHOLD
) -> bool:
    """
    Check whether the stock is RSI oversold.

    Parameters
    ----------
    df : DataFrame

    length : int

    threshold : float

    Returns
    -------
    bool
    """

    if len(df) < length + 5:
        return False

    df = df.copy()

    df["RSI"] = calculate_rsi(df, length)

    latest_rsi = df["RSI"].iloc[-1]

    if pd.isna(latest_rsi):
        return False

    return latest_rsi < threshold


def latest_value(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH
) -> float:
    """
    Return latest RSI value.

    Useful for displaying in Streamlit.
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

    result = screen(df)

    print(f"Symbol : {symbol}")
    print(f"Latest RSI : {latest_value(df)}")
    print(f"Oversold : {result}")
