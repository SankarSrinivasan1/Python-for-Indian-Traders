"""
Screener Manager

Runs the selected screener and
returns the result.

Add new screening strategies here.
"""

from screeners.rsi_oversold import screen as rsi_oversold
from screeners.rsi_overbought import screen as rsi_overbought
from screeners.golden_cross import screen as golden_cross
from screeners.supertrend_buy import screen as supertrend_buy
from screeners.adx_trend import screen as adx_trend
from screeners.bollinger_breakout import screen as bollinger_breakout


SCREENERS = {
    "RSI Oversold": rsi_oversold,
    "RSI Overbought": rsi_overbought,
    "Golden Cross": golden_cross,
    "Supertrend Buy": supertrend_buy,
    "ADX Strong Trend": adx_trend,
    "Bollinger Breakout": bollinger_breakout,
}


def get_available_screeners():
    """
    Return all screener names.
    """
    return list(SCREENERS.keys())


def run_screener(
    screener_name: str,
    dataframe,
    **kwargs
):
    """
    Execute the selected screener.

    Parameters
    ----------
    screener_name : str
        Name of the screener

    dataframe : pandas.DataFrame
        OHLCV data

    kwargs
        Optional parameters

    Returns
    -------
    bool
    """

    if screener_name not in SCREENERS:
        raise ValueError(
            f"Unknown Screener: {screener_name}"
        )

    screener = SCREENERS[screener_name]

    return screener(
        dataframe,
        **kwargs
    )


if __name__ == "__main__":

    import yfinance as yf

    symbol = "RELIANCE.NS"

    df = yf.download(
        symbol,
        period="1y",
        progress=False
    )

    print("=" * 50)

    for name in get_available_screeners():

        result = run_screener(name, df)

        print(f"{name:<25} : {result}")
