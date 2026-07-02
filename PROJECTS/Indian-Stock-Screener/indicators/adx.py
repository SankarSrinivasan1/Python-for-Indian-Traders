"""
Average Directional Index (ADX)

Calculates ADX, +DI and -DI using pandas-ta.

Author:
Python for Indian Stock Traders
"""

import pandas as pd
import pandas_ta as ta


def calculate_adx(
    data: pd.DataFrame,
    length: int = 14
) -> pd.DataFrame:
    """
    Calculate ADX indicator.
    """

    required = ["High", "Low", "Close"]

    for col in required:
        if col not in data.columns:
            raise ValueError(f"{col} column not found.")

    df = data.copy()

    adx = ta.adx(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=length
    )

    df = pd.concat([df, adx], axis=1)

    return df


def get_adx_column(df: pd.DataFrame) -> str:

    cols = [c for c in df.columns if c.startswith("ADX_")]

    if not cols:
        raise ValueError("ADX column not found.")

    return cols[0]


def get_plus_di_column(df: pd.DataFrame) -> str:

    cols = [c for c in df.columns if c.startswith("DMP_")]

    if not cols:
        raise ValueError("+DI column not found.")

    return cols[0]


def get_minus_di_column(df: pd.DataFrame) -> str:

    cols = [c for c in df.columns if c.startswith("DMN_")]

    if not cols:
        raise ValueError("-DI column not found.")

    return cols[0]


def is_strong_trend(
    df: pd.DataFrame,
    threshold: float = 25
) -> bool:

    adx = get_adx_column(df)

    return df[adx].iloc[-1] >= threshold


def is_bullish_trend(df: pd.DataFrame) -> bool:

    plus = get_plus_di_column(df)
    minus = get_minus_di_column(df)

    return df[plus].iloc[-1] > df[minus].iloc[-1]


def is_bearish_trend(df: pd.DataFrame) -> bool:

    plus = get_plus_di_column(df)
    minus = get_minus_di_column(df)

    return df[plus].iloc[-1] < df[minus].iloc[-1]


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    df = calculate_adx(df)

    print(df.tail())

    print("Strong Trend :", is_strong_trend(df))
    print("Bullish :", is_bullish_trend(df))
    print("Bearish :", is_bearish_trend(df))
