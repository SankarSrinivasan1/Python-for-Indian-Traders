"""
Unit tests for Supertrend indicator.
"""

import pandas as pd
import numpy as np

from indicators.supertrend import calculate_supertrend


def sample_data():
    np.random.seed(100)

    close = np.random.normal(100, 1.5, 250).cumsum() / 10 + 100

    high = close + np.random.uniform(0.5, 2.0, 250)
    low = close - np.random.uniform(0.5, 2.0, 250)

    return pd.DataFrame({
        "High": high,
        "Low": low,
        "Close": close
    })


def test_supertrend_column_exists():
    df = sample_data()

    result = calculate_supertrend(df)

    assert "Supertrend" in result.columns


def test_supertrend_length():
    df = sample_data()

    result = calculate_supertrend(df)

    assert len(result) == len(df)


def test_supertrend_not_all_nan():
    df = sample_data()

    result = calculate_supertrend(df)

    assert result["Supertrend"].notna().sum() > 0


def test_supertrend_boolean_signal():
    df = sample_data()

    result = calculate_supertrend(df)

    if "BuySignal" in result.columns:
        assert result["BuySignal"].isin([True, False]).all()
