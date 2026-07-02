"""
Bollinger Bands

Uses pandas-ta.

Author:
Python for Indian Stock Traders
"""

import pandas as pd
import pandas_ta as ta


def calculate_bollinger(
    data: pd.DataFrame,
    length: int = 20,
    std: float = 2.0
) -> pd.DataFrame:
    """
    Calculate Bollinger Bands.
    """

    if "Close" not in data.columns:
        raise ValueError("Close column not found.")

    df = data.copy()

    bb = ta.bbands(
        close=df["Close"],
        length=length,
        std=std
    )

    df = pd.concat([df, bb], axis=1)

    return df


def get_upper_band(df: pd.DataFrame) -> str:

    cols = [c for c in df.columns if c.startswith("BBU_")]

    if not cols:
        raise ValueError("Upper Band not found.")

    return cols[0]


def get_middle_band(df: pd.DataFrame) -> str:

    cols = [c for c in df.columns if c.startswith("BBM_")]

    if not cols:
        raise ValueError("Middle Band not found.")

    return cols[0]


def get_lower_band(df: pd.DataFrame) -> str:

    cols = [c for c in df.columns if c.startswith("BBL_")]

    if not cols:
        raise ValueError("Lower Band not found.")

    return cols[0]


def is_upper_breakout(df: pd.DataFrame) -> bool:

    upper = get_upper_band(df)

    return df["Close"].iloc[-1] > df[upper].iloc[-1]


def is_lower_breakdown(df: pd.DataFrame) -> bool:

    lower = get_lower_band(df)

    return df["Close"].iloc[-1] < df[lower].iloc[-1]


def inside_bands(df: pd.DataFrame) -> bool:

    upper = get_upper_band(df)
    lower = get_lower_band(df)

    close = df["Close"].iloc[-1]

    return lower <= close <= upper


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    df = calculate_bollinger(df)

    print(df.tail())

    print("Upper Breakout :", is_upper_breakout(df))
    print("Lower Breakdown :", is_lower_breakdown(df))
