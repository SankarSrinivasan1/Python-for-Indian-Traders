"""
Unit tests for screener modules.
"""

import pandas as pd
import numpy as np

from screeners.rsi_oversold import screen_rsi_oversold
from screeners.rsi_overbought import screen_rsi_overbought
from screeners.golden_cross import screen_golden_cross
from screeners.supertrend_buy import screen_supertrend_buy
from screeners.adx_trend import screen_adx_trend
from screeners.bollinger_breakout import screen_bollinger_breakout


def sample_data():
    np.random.seed(500)

    close = np.random.normal(100, 2, 250).cumsum() / 10 + 100

    high = close + np.random.uniform(0.5, 2.0, 250)
    low = close - np.random.uniform(0.5, 2.0, 250)
    volume = np.random.randint(100000, 1000000, 250)

    return pd.DataFrame({
        "High": high,
        "Low": low,
        "Close": close,
        "Volume": volume
    })


def test_rsi_oversold_returns_dataframe():
    result = screen_rsi_oversold(sample_data())
    assert isinstance(result, pd.DataFrame)


def test_rsi_overbought_returns_dataframe():
    result = screen_rsi_overbought(sample_data())
    assert isinstance(result, pd.DataFrame)


def test_golden_cross_returns_dataframe():
    result = screen_golden_cross(sample_data())
    assert isinstance(result, pd.DataFrame)


def test_supertrend_returns_dataframe():
    result = screen_supertrend_buy(sample_data())
    assert isinstance(result, pd.DataFrame)


def test_adx_returns_dataframe():
    result = screen_adx_trend(sample_data())
    assert isinstance(result, pd.DataFrame)


def test_bollinger_returns_dataframe():
    result = screen_bollinger_breakout(sample_data())
    assert isinstance(result, pd.DataFrame)


def test_dataframe_columns_preserved():
    result = screen_rsi_oversold(sample_data())

    expected_columns = [
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    for col in expected_columns:
        assert col in result.columns
