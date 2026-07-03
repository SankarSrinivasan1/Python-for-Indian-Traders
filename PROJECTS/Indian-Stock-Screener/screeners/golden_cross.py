"""
Golden Cross Screener

Condition

50 EMA crosses above 200 EMA
"""

import pandas as pd
import pandas_ta as ta

FAST_EMA = 50
SLOW_EMA = 200


def calculate_ema(
    df: pd.DataFrame,
    fast: int = FAST_EMA,
    slow: int = SLOW_EMA
):
    """
    Calculate both EMAs.
    """

    ema_fast = ta.ema(df["Close"], length=fast)
    ema_slow = ta.ema(df["Close"], length=slow)

    return ema_fast, ema_slow


def screen(
    df: pd.DataFrame,
    fast: int = FAST_EMA,
    slow: int = SLOW_EMA
) -> bool:
    """
    Detect Golden Cross.
    """

    if len(df) < slow + 5:
        return False

    df = df.copy()

    df["EMA_FAST"], df["EMA_SLOW"] = calculate_ema(
        df,
        fast,
        slow
    )

    prev_fast = df["EMA_FAST"].iloc[-2]
    prev_slow = df["EMA_SLOW"].iloc[-2]

    curr_fast = df["EMA_FAST"].iloc[-1]
    curr_slow = df["EMA_SLOW"].iloc[-1]

    if (
        pd.isna(prev_fast)
        or pd.isna(prev_slow)
        or pd.isna(curr_fast)
        or pd.isna(curr_slow)
    ):
        return False

    crossed = (
        prev_fast <= prev_slow
        and curr_fast > curr_slow
    )

    return crossed


def latest_values(
    df: pd.DataFrame,
    fast: int = FAST_EMA,
    slow: int = SLOW_EMA
):
    """
    Returns latest EMA values.
    """

    ema_fast, ema_slow = calculate_ema(
        df,
        fast,
        slow
    )

    return {
        "EMA50": round(float(ema_fast.iloc[-1]), 2),
        "EMA200": round(float(ema_slow.iloc[-1]), 2),
    }


if __name__ == "__main__":

    import yfinance as yf

    symbol = "RELIANCE.NS"

    df = yf.download(
        symbol,
        period="2y",
        progress=False
    )

    print(latest_values(df))
    print("Golden Cross :", screen(df))
