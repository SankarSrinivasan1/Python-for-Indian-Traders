"""
Data Source Package

This package provides modules for downloading and managing
Indian stock market data from multiple sources.

Modules
-------
yahoo_data.py
    Download OHLCV data using Yahoo Finance.

nse_data.py
    Download market data from NSE (optional).

downloader.py
    Unified interface for downloading data.

cache_manager.py
    Handles local caching of downloaded data.
"""

__version__ = "1.0.0"

from .yahoo_data import YahooData
