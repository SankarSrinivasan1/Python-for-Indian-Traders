"""
yahoo_data.py

Download Indian stock market data from Yahoo Finance.
"""

import yfinance as yf
import pandas as pd


class YahooData:
    """
    Downloads historical stock data from Yahoo Finance.
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
        Download historical OHLCV data.

        Parameters
        ----------
        symbol : str
            NSE symbol without .NS
            Example:
                RELIANCE

        period : str
            1mo
            3mo
            6mo
            1y
            2y
            5y
            max

        interval : str
            1d
            1wk
            1mo

        Returns
        -------
        pandas.DataFrame
        """

        ticker = f"{symbol}.NS"

        try:

            data = yf.download(
                ticker,
                period=period,
                interval=interval,
                progress=False,
                auto_adjust=True
            )

            if data.empty:
                print(f"No data found for {symbol}")
                return pd.DataFrame()

            data.reset_index(inplace=True)

            data.columns = [
                str(col).replace(" ", "_")
                for col in data.columns
            ]

            return data

        except Exception as e:

            print(f"Error downloading {symbol}: {e}")
            return pd.DataFrame()

    def download_multiple(
        self,
        symbols,
        period="6mo",
        interval="1d"
    ):
        """
        Download multiple stocks.

        Parameters
        ----------
        symbols : list

        Returns
        -------
        dict
            {
                "RELIANCE": dataframe,
                "TCS": dataframe
            }
        """

        results = {}

        for symbol in symbols:

            results[symbol] = self.download_stock(
                symbol,
                period,
                interval
            )

        return results
