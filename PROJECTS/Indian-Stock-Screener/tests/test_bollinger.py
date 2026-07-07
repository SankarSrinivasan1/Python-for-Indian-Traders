"""
Unit tests for Bollinger Bands.
"""

import pandas as pd
import numpy as np

from indicators.bollinger import calculate_bollinger


def sample_data():
    np.random.seed(300)

    close = np.random.normal(100, 2, 250).cumsum() / 10 + 100

    return pd.DataFrame({
        "Close": close
    })


def test_columns_exist():
    df = sample_data()

    result = calculate_bollinger(df)

    assert "BB_Upper" in result.columns
    assert "BB_Middle" in result.columns
    assert "BB_Lower" in result.columns


def test_band_relationship():
    df = sample_data()

    result = calculate_bollinger(df)

    valid = result.dropna()

    assert (valid["BB_Upper"] >= valid["BB_Middle"]).all()
    assert (valid["BB_Middle"] >= valid["BB_Lower"]).all()


def test_dataframe_length():
    df = sample_data()

    result = calculate_bollinger(df)

    assert len(result) == len(df)


def test_not_all_nan():
    df = sample_data()

    result = calculate_bollinger(df)

    assert result["BB_Upper"].notna().sum() > 0
