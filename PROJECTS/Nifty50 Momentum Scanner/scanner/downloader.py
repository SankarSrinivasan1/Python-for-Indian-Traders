"""
downloader.py

Project:
Nifty 50 Momentum Scanner

Purpose:
--------
Responsible for downloading historical market data for one or more stocks
using Yahoo Finance (yfinance).

This module intentionally keeps all download logic separate from indicator
calculations and scoring to keep the project modular.

Author:
Python for Indian Stock Traders

------------------------------------------------------------
Future Improvements
------------------------------------------------------------

TODO:
- Retry failed downloads
- Parallel downloads
- Local caching
- Progress bar
- Download logging
- API fallback
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd
import yfinance as yf

# ==========================================================
# Configuration
# ==========================================================

DEFAULT_PERIOD = "6mo"
DEFAULT_INTERVAL = "1d"

CACHE_DIRECTORY = Path("data")

# Create data directory automatically
CACHE_DIRECTORY.mkdir(exist_ok=True)

# ==========================================================
# Utility Functions
# ==========================================================


def format_symbol(symbol: str) -> str:
    """
    Convert NSE symbol into Yahoo Finance format.

    Example
    -------
    RELIANCE -> RELIANCE.NS

    Notes
    -----
    If ".NS" already exists, do nothing.
    """

    symbol = symbol.strip().upper()

    if symbol.endswith(".NS"):
        return symbol

    return f"{symbol}.NS"


# ==========================================================
# Single Stock Downloader
# ==========================================================


def download_stock(
    symbol: str,
    period: str = DEFAULT_PERIOD,
    interval: str = DEFAULT_INTERVAL,
    auto_adjust: bool = True,
) -> pd.DataFrame:
    """
    Download historical OHLCV data for one stock.

    Parameters
    ----------
    symbol : str
        NSE symbol

    period : str
        Example:
            1mo
            3mo
            6mo
            1y
            2y

    interval : str
        Example:
            1d
            1h
            30m

    Returns
    -------
    pandas.DataFrame

    Columns usually include

        Open
        High
        Low
        Close
        Volume

    Empty DataFrame is returned if download fails.
    """

    yahoo_symbol = format_symbol(symbol)

    try:

        data = yf.download(
            tickers=yahoo_symbol,
            period=period,
            interval=interval,
            auto_adjust=auto_adjust,
            progress=False,
        )

        if data.empty:
            print(f"[WARNING] No data found for {symbol}")
            return pd.DataFrame()

        data = data.copy()

        data.reset_index(inplace=True)

        return data

    except Exception as exc:

        print(f"[ERROR] Failed downloading {symbol}")

        print(exc)

        return pd.DataFrame()


# ==========================================================
# Multiple Stock Downloader
# ==========================================================


def download_multiple(
    symbols: List[str],
    period: str = DEFAULT_PERIOD,
    interval: str = DEFAULT_INTERVAL,
) -> Dict[str, pd.DataFrame]:
    """
    Download historical data for multiple stocks.

    Parameters
    ----------
    symbols : list

    Returns
    -------
    Dictionary

    Example

    {
        "RELIANCE": dataframe,
        "TCS": dataframe,
        ...
    }
    """

    market_data = {}

    total = len(symbols)

    for index, symbol in enumerate(symbols, start=1):

        print(f"[{index}/{total}] Downloading {symbol}")

        df = download_stock(
            symbol=symbol,
            period=period,
            interval=interval,
        )

        if not df.empty:
            market_data[symbol] = df

    print()

    print(f"Downloaded {len(market_data)} stocks successfully.")

    return market_data


# ==========================================================
# Cache Functions
# ==========================================================


def save_cache(
    symbol: str,
    dataframe: pd.DataFrame,
    folder: Path = CACHE_DIRECTORY,
) -> None:
    """
    Save downloaded data to CSV.

    Example

    data/
        RELIANCE.csv
        TCS.csv
    """

    if dataframe.empty:
        return

    filepath = folder / f"{symbol.upper()}.csv"

    dataframe.to_csv(filepath, index=False)


def load_cache(
    symbol: str,
    folder: Path = CACHE_DIRECTORY,
) -> Optional[pd.DataFrame]:
    """
    Load cached CSV if available.

    Returns
    -------
    DataFrame

    or

    None
    """

    filepath = folder / f"{symbol.upper()}.csv"

    if not filepath.exists():
        return None

    try:

        return pd.read_csv(filepath)

    except Exception:

        return None


# ==========================================================
# Download + Cache
# ==========================================================


def download_and_cache(
    symbol: str,
    period: str = DEFAULT_PERIOD,
    interval: str = DEFAULT_INTERVAL,
) -> pd.DataFrame:
    """
    Download a stock and automatically save it locally.
    """

    df = download_stock(
        symbol=symbol,
        period=period,
        interval=interval,
    )

    if not df.empty:
        save_cache(symbol, df)

    return df


# ==========================================================
# Refresh Entire Cache
# ==========================================================


def refresh_cache(
    symbols: List[str],
    period: str = DEFAULT_PERIOD,
    interval: str = DEFAULT_INTERVAL,
) -> Dict[str, pd.DataFrame]:
    """
    Download all stocks and refresh local cache.

    Returns
    -------
    Dictionary of DataFrames
    """

    market_data = {}

    for symbol in symbols:

        df = download_and_cache(
            symbol=symbol,
            period=period,
            interval=interval,
        )

        if not df.empty:
            market_data[symbol] = df

    return market_data


# ==========================================================
# Placeholder Functions (Future Versions)
# ==========================================================


def download_intraday(symbol: str):
    """
    TODO

    Future Version

    Download intraday data.

    Possible intervals

        1m
        2m
        5m
        15m
        30m
        60m
    """
    raise NotImplementedError


def download_weekly(symbol: str):
    """
    TODO

    Download weekly candles.
    """
    raise NotImplementedError


def download_monthly(symbol: str):
    """
    TODO

    Download monthly candles.
    """
    raise NotImplementedError


def retry_failed_download(symbol: str):
    """
    TODO

    Retry logic with exponential backoff.
    """
    raise NotImplementedError


def download_parallel(symbols: List[str]):
    """
    TODO

    Future enhancement using

    concurrent.futures

    or

    multiprocessing

    to speed up downloads.
    """
    raise NotImplementedError


# ==========================================================
# Module Test
# ==========================================================

if __name__ == "__main__":

    sample_symbol = "RELIANCE"

    print("=" * 60)
    print("Testing downloader.py")
    print("=" * 60)

    data = download_stock(sample_symbol)

    if not data.empty:

        print(data.tail())

        save_cache(sample_symbol, data)

        print()

        print("Download successful.")

    else:

        print("Download failed.")
