"""
nse_data.py

Placeholder for downloading stock data directly from NSE.

This module provides a common interface so the project can
switch between Yahoo Finance and NSE with minimal changes.
"""

import pandas as pd


class NSEData:
    """
    NSE Data Source

    Future versions can integrate:

    - NSE Official APIs
    - nsepython
    - NSE India website
    """

    def __init__(self):
        pass

    def download_stock(
        self,
        symbol,
        period="6mo",
        interval="1d"
    ):
        """
        Download one stock.

        Currently not implemented.
        """

        print(
            f"NSE download for {symbol} is not implemented yet."
        )

        return pd.DataFrame()

    def download_multiple(
        self,
        symbols,
        period="6mo",
        interval="1d"
    ):
        """
        Download multiple stocks.
        """

        data = {}

        for symbol in symbols:

            data[symbol] = self.download_stock(
                symbol,
                period,
                interval
            )

        return data
