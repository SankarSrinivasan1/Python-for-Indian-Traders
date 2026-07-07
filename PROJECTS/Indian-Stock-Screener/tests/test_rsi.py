"""
Unit tests for RSI indicator.
"""

import pandas as pd
import numpy as np

from indicators.rsi import calculate_rsi


def sample_data():
    np.random.seed(42)

    close = np.random.normal(100, 2, 250).cumsum() / 10 + 100

    return pd.DataFrame({
        "Close": close
    })


def test_rsi_column_exists():
    df = sample_data()

    result = calculate_rsi(df)

    assert "RSI" in result.columns


def test_rsi_not_empty():
    df = sample_data()

    result = calculate_rsi(df)

    assert result["RSI"].dropna().shape[0] > 0


def test_rsi_range():
    df = sample_data()

    result = calculate_rsi(df)

    rsi = result["RSI"].dropna()

    assert (rsi >= 0).all()
    assert (rsi <= 100).all()


def test_rsi_dataframe_length():
    df = sample_data()

    result = calculate_rsi(df)

    assert len(df) == len(result)
