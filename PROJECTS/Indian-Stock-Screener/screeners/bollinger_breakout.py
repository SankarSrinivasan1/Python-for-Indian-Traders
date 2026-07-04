"""
Bollinger Band Breakout Screener

Condition

Latest Close > Upper Bollinger Band
"""

import pandas as pd
import pandas_ta as ta

DEFAULT_LENGTH = 20
DEFAULT_STD = 2.0


def calculate_bbands(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    std: float = DEFAULT_STD
) -> pd.DataFrame:
    """
    Calculate Bollinger Bands.
    """
    return ta.bbands(
        close=df["Close"],
        length=length,
        std=std
    )


def screen(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    std: float = DEFAULT_STD
) -> bool:
    """
    Returns True if price breaks above
    the upper Bollinger Band.
    """

    if len(df) < length + 5:
        return False

    df = df.copy()

    bb = calculate_bbands(df, length, std)

    upper_band = bb.iloc[:, 2].iloc[-1]
    latest_close = df["Close"].iloc[-1]

    if pd.isna(upper_band):
        return False

    return latest_close > upper_band


def latest_values(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    std: float = DEFAULT_STD
):
    """
    Returns latest Bollinger values.
    """

    bb = calculate_bbands(df, length, std)

    return {
        "Upper": round(float(bb.iloc[:, 2].iloc[-1]), 2),
        "Middle": round(float(bb.iloc[:, 1].iloc[-1]), 2),
        "Lower": round(float(bb.iloc[:, 0].iloc[-1]), 2),
    }


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    print(latest_values(df))
    print("Breakout :", screen(df))
