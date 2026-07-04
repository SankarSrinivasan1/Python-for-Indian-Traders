"""
downloader.py

Unified interface for downloading stock data from
different providers.

Example

downloader = StockDownloader(source="yahoo")

df = downloader.download("RELIANCE")
"""

from .yahoo_data import YahooData
from .nse_data import NSEData


class StockDownloader:
    """
    Main data download manager.
    """

    def __init__(self, source="yahoo"):

        self.source = source.lower()

        if self.source == "yahoo":
            self.provider = YahooData()

        elif self.source == "nse":
            self.provider = NSEData()

        else:
            raise ValueError(
                "Supported sources are: yahoo, nse"
            )

    def download(
        self,
        symbol,
        period="6mo",
        interval="1d"
    ):
        """
        Download one stock.
        """

        return self.provider.download_stock(
            symbol,
            period,
            interval
        )

    def download_many(
        self,
        symbols,
        period="6mo",
        interval="1d"
    ):
        """
        Download multiple stocks.
        """

        return self.provider.download_multiple(
            symbols,
            period,
            interval
        )
