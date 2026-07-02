"""
Supertrend Indicator

Uses pandas-ta implementation.

Author:
Python for Indian Stock Traders
"""

import pandas as pd
import pandas_ta as ta


def calculate_supertrend(
    data: pd.DataFrame,
    length: int = 10,
    multiplier: float = 3.0
) -> pd.DataFrame:
    """
    Calculate Supertrend.

    Parameters
    ----------
    data : DataFrame

    length : ATR Length

    multiplier : ATR Multiplier

    Returns
    -------
    DataFrame
    """

    required = ["High", "Low", "Close"]

    for col in required:
        if col not in data.columns:
            raise ValueError(f"{col} column missing.")

    df = data.copy()

    st = ta.supertrend(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        length=length,
        multiplier=multiplier
    )

    df = pd.concat([df, st], axis=1)

    return df


def get_supertrend_column(
    df: pd.DataFrame
) -> str:
    """
    Return Supertrend value column.
    """

    cols = [
        c for c in df.columns
        if c.startswith("SUPERT_")
    ]

    if not cols:
        raise ValueError("Supertrend column not found.")

    return cols[0]


def get_direction_column(
    df: pd.DataFrame
) -> str:
    """
    Return Supertrend direction column.
    """

    cols = [
        c for c in df.columns
        if c.startswith("SUPERTd_")
    ]

    if not cols:
        raise ValueError("Direction column not found.")

    return cols[0]


def is_supertrend_buy(
    df: pd.DataFrame
) -> bool:
    """
    Buy signal when direction == 1
    """

    direction = get_direction_column(df)

    return df[direction].iloc[-1] == 1


def is_supertrend_sell(
    df: pd.DataFrame
) -> bool:
    """
    Sell signal when direction == -1
    """

    direction = get_direction_column(df)

    return df[direction].iloc[-1] == -1


def latest_supertrend_value(
    df: pd.DataFrame
) -> float:
    """
    Latest Supertrend value.
    """

    st_col = get_supertrend_column(df)

    return float(df[st_col].iloc[-1])


if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )

    df = calculate_supertrend(df)

    print(df.tail())

    print("Buy Signal :", is_supertrend_buy(df))
    print("Sell Signal :", is_supertrend_sell(df))

    print(
        "Latest Supertrend :",
        latest_supertrend_value(df)
    )
