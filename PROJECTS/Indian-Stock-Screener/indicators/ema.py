"""
Exponential Moving Average (EMA)

Provides reusable EMA calculation functions using pandas-ta.

Author:
Python for Indian Stock Traders
"""

import pandas as pd
import pandas_ta as ta


def calculate_ema(
    data: pd.DataFrame,
    length: int = 20,
    price_column: str = "Close"
) -> pd.DataFrame:
    """
    Calculate Exponential Moving Average.

    Parameters
    ----------
    data : pd.DataFrame
        OHLCV DataFrame

    length : int
        EMA period

    price_column : str
        Price column name

    Returns
    -------
    pd.DataFrame
    """

    if price_column not in data.columns:
        raise ValueError(f"'{price_column}' column not found.")

    df = data.copy()

    ema_column = f"EMA_{length}"

    df[ema_column] = ta.ema(
        close=df[price_column],
        length=length
    )

    return df


def calculate_multiple_ema(
    data: pd.DataFrame,
    periods: list = [20, 50, 100, 200],
    price_column: str = "Close"
) -> pd.DataFrame:
    """
    Calculate multiple EMAs.
    """

    df = data.copy()

    for period in periods:
        df = calculate_ema(
            df,
            length=period,
            price_column=price_column
        )

    return df


def is_golden_cross(
    data: pd.DataFrame,
    short_period: int = 50,
    long_period: int = 200
) -> bool:
    """
    Returns True if Golden Cross occurred
    on the latest candle.
    """

    short_col = f"EMA_{short_period}"
    long_col = f"EMA_{long_period}"

    if short_col not in data.columns:
        raise ValueError(f"{short_col} missing.")

    if long_col not in data.columns:
        raise ValueError(f"{long_col} missing.")

    if len(data) < 2:
        return False

    prev_short = data[short_col].iloc[-2]
    prev_long = data[long_col].iloc[-2]

    curr_short = data[short_col].iloc[-1]
    curr_long = data[long_col].iloc[-1]

    return (
        prev_short <= prev_long
        and curr_short > curr_long
    )


def is_death_cross(
    data: pd.DataFrame,
    short_period: int = 50,
    long_period: int = 200
) -> bool:
    """
    Returns True if Death Cross occurred.
    """

    short_col = f"EMA_{short_period}"
    long_col = f"EMA_{long_period}"

    if len(data) < 2:
        return False

    prev_short = data[short_col].iloc[-2]
    prev_long = data[long_col].iloc[-2]

    curr_short = data[short_col].iloc[-1]
    curr_long = data[long_col].iloc[-1]

    return (
        prev_short >= prev_long
        and curr_short < curr_long
    )


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    df = calculate_multiple_ema(df)

    print(df.tail())

    print("Golden Cross :", is_golden_cross(df))
    print("Death Cross :", is_death_cross(df))
