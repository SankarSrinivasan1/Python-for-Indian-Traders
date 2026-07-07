"""
Unit tests for ADX indicator.
"""

import pandas as pd
import numpy as np

from indicators.adx import calculate_adx


def sample_data():
    np.random.seed(200)

    close = np.random.normal(100, 1.8, 250).cumsum() / 10 + 100
    high = close + np.random.uniform(0.5, 2.0, 250)
    low = close - np.random.uniform(0.5, 2.0, 250)

    return pd.DataFrame({
        "High": high,
        "Low": low,
        "Close": close
    })


def test_adx_column_exists():
    df = sample_data()

    result = calculate_adx(df)

    assert "ADX" in result.columns


def test_adx_not_empty():
    df = sample_data()

    result = calculate_adx(df)

    assert result["ADX"].dropna().shape[0] > 0


def test_adx_positive():
    df = sample_data()

    result = calculate_adx(df)

    adx = result["ADX"].dropna()

    assert (adx >= 0).all()


def test_dataframe_length():
    df = sample_data()

    result = calculate_adx(df)

    assert len(result) == len(df)
