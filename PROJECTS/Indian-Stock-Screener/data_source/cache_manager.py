"""
cache_manager.py

Local cache manager for downloaded stock data.

Features
--------
- Save DataFrame to CSV
- Load cached data
- Check if cache exists
- Delete cache
- Clear all cached files
"""

from pathlib import Path
import pandas as pd


class CacheManager:
    """
    Handles local CSV cache.
    """

    def __init__(self, cache_dir="data/cache"):

        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _file_path(self, symbol):
        """
        Returns cache filename.
        """

        return self.cache_dir / f"{symbol.upper()}.csv"

    def exists(self, symbol):
        """
        Check whether cache exists.
        """

        return self._file_path(symbol).exists()

    def save(self, symbol, dataframe):
        """
        Save DataFrame to cache.
        """

        if dataframe is None:
            return

        if dataframe.empty:
            return

        dataframe.to_csv(
            self._file_path(symbol),
            index=False
        )

    def load(self, symbol):
        """
        Load cached DataFrame.

        Returns empty DataFrame if file does not exist.
        """

        file = self._file_path(symbol)

        if not file.exists():
            return pd.DataFrame()

        return pd.read_csv(file)

    def delete(self, symbol):
        """
        Delete one cached file.
        """

        file = self._file_path(symbol)

        if file.exists():
            file.unlink()

    def clear(self):
        """
        Delete all cached files.
        """

        for file in self.cache_dir.glob("*.csv"):
            file.unlink()

    def list_cached_symbols(self):
        """
        Returns list of cached symbols.
        """

        return sorted(
            file.stem
            for file in self.cache_dir.glob("*.csv")
        )
