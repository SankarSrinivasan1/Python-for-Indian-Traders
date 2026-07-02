"""
Relative Strength Index (RSI)

Calculates the RSI indicator using pandas-ta.

Author:
Python for Indian Stock Traders
"""

import pandas as pd
import pandas_ta as ta


def calculate_rsi(
    data: pd.DataFrame,
    length: int = 14,
    price_column: str = "Close"
) -> pd.DataFrame:
    """
    Calculate Relative Strength Index.

    Parameters
    ----------
    data : pd.DataFrame
        OHLCV dataframe.

    length : int
        RSI period.

    price_column : str
        Price column.

    Returns
    -------
    pd.DataFrame
        Original dataframe with RSI column.
    """

    if price_column not in data.columns:
        raise ValueError(
            f"Column '{price_column}' not found in dataframe."
        )

    df = data.copy()

    df["RSI"] = ta.rsi(
        close=df[price_column],
        length=length
    )

    return df


def is_oversold(
    data: pd.DataFrame,
    threshold: float = 30
) -> bool:
    """
    Returns True if latest RSI is below threshold.
    """

    latest = data["RSI"].iloc[-1]

    if pd.isna(latest):
        return False

    return latest < threshold


def is_overbought(
    data: pd.DataFrame,
    threshold: float = 70
) -> bool:
    """
    Returns True if latest RSI is above threshold.
    """

    latest = data["RSI"].iloc[-1]

    if pd.isna(latest):
        return False

    return latest > threshold


if __name__ == "__main__":

    import yfinance as yf

    ticker = "RELIANCE.NS"

    df = yf.download(
        ticker,
        period="6mo",
        progress=False
    )

    df = calculate_rsi(df)

    print(df.tail())

    print("Oversold :", is_oversold(df))
    print("Overbought :", is_overbought(df))
