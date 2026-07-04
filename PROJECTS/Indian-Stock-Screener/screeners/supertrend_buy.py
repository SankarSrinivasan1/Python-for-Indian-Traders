"""
Supertrend Buy Screener

Condition:
Close > Supertrend
Trend Direction = Bullish
"""

import pandas as pd
import pandas_ta as ta

DEFAULT_LENGTH = 10
DEFAULT_MULTIPLIER = 3.0


def calculate_supertrend(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    multiplier: float = DEFAULT_MULTIPLIER
):
    """
    Calculate Supertrend.
    """

    st = ta.supertrend(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=length,
        multiplier=multiplier
    )

    return st


def screen(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    multiplier: float = DEFAULT_MULTIPLIER
) -> bool:

    if len(df) < length + 10:
        return False

    df = df.copy()

    st = calculate_supertrend(df, length, multiplier)

    direction = st.iloc[:, 1].iloc[-1]

    return direction == 1


def latest_direction(
    df: pd.DataFrame,
    length: int = DEFAULT_LENGTH,
    multiplier: float = DEFAULT_MULTIPLIER
):

    st = calculate_supertrend(df, length, multiplier)

    direction = st.iloc[:, 1].iloc[-1]

    return "Bullish" if direction == 1 else "Bearish"


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    print(latest_direction(df))
    print(screen(df))
