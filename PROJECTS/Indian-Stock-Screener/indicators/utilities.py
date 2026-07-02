"""
Utility Functions for Technical Indicators

Shared helper functions used throughout the indicators package.

Author:
Python for Indian Stock Traders
"""

from typing import List, Optional

import numpy as np
import pandas as pd


# ---------------------------------------------------------
# Required OHLC Columns
# ---------------------------------------------------------

REQUIRED_OHLC_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Close"
]

REQUIRED_OHLCV_COLUMNS = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]


# ---------------------------------------------------------
# Validation Functions
# ---------------------------------------------------------

def validate_columns(
    data: pd.DataFrame,
    required_columns: List[str]
) -> None:
    """
    Validate required dataframe columns.

    Raises
    ------
    ValueError
        If one or more required columns are missing.
    """

    missing = [
        col for col in required_columns
        if col not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {', '.join(missing)}"
        )


def validate_ohlc(
    data: pd.DataFrame
) -> None:
    """
    Validate OHLC dataframe.
    """

    validate_columns(
        data,
        REQUIRED_OHLC_COLUMNS
    )


def validate_ohlcv(
    data: pd.DataFrame
) -> None:
    """
    Validate OHLCV dataframe.
    """

    validate_columns(
        data,
        REQUIRED_OHLCV_COLUMNS
    )


# ---------------------------------------------------------
# Data Cleaning
# ---------------------------------------------------------

def remove_nan_rows(
    data: pd.DataFrame
) -> pd.DataFrame:
    """
    Remove rows containing NaN values.
    """

    return data.dropna().copy()


def fill_nan(
    data: pd.DataFrame,
    method: str = "ffill"
) -> pd.DataFrame:
    """
    Fill missing values.

    method:
        ffill
        bfill
    """

    df = data.copy()

    if method == "ffill":
        return df.ffill()

    if method == "bfill":
        return df.bfill()

    raise ValueError("method must be 'ffill' or 'bfill'")


# ---------------------------------------------------------
# Latest Value Helpers
# ---------------------------------------------------------

def latest_value(
    data: pd.DataFrame,
    column: str
):
    """
    Return latest value.
    """

    if column not in data.columns:
        raise ValueError(f"{column} not found.")

    return data[column].iloc[-1]


def previous_value(
    data: pd.DataFrame,
    column: str
):
    """
    Return previous candle value.
    """

    if column not in data.columns:
        raise ValueError(f"{column} not found.")

    return data[column].iloc[-2]


# ---------------------------------------------------------
# Indicator Helpers
# ---------------------------------------------------------

def column_exists(
    data: pd.DataFrame,
    column: str
) -> bool:
    """
    Check whether a column exists.
    """

    return column in data.columns


def find_column_by_prefix(
    data: pd.DataFrame,
    prefix: str
) -> Optional[str]:
    """
    Find first column beginning with prefix.
    """

    cols = [
        col
        for col in data.columns
        if col.startswith(prefix)
    ]

    if cols:
        return cols[0]

    return None


# ---------------------------------------------------------
# Price Calculations
# ---------------------------------------------------------

def percentage_change(
    current: float,
    previous: float
) -> float:
    """
    Percentage change.
    """

    if previous == 0:
        return 0.0

    return ((current - previous) / previous) * 100


def latest_return(
    data: pd.DataFrame,
    column: str = "Close"
) -> float:
    """
    Return latest daily percentage move.
    """

    current = latest_value(data, column)
    previous = previous_value(data, column)

    return percentage_change(
        current,
        previous
    )


# ---------------------------------------------------------
# Signal Helpers
# ---------------------------------------------------------

def crossover(
    series1: pd.Series,
    series2: pd.Series
) -> bool:
    """
    Detect bullish crossover.
    """

    return (
        series1.iloc[-2] <= series2.iloc[-2]
        and
        series1.iloc[-1] > series2.iloc[-1]
    )


def crossunder(
    series1: pd.Series,
    series2: pd.Series
) -> bool:
    """
    Detect bearish crossover.
    """

    return (
        series1.iloc[-2] >= series2.iloc[-2]
        and
        series1.iloc[-1] < series2.iloc[-1]
    )


# ---------------------------------------------------------
# Formatting
# ---------------------------------------------------------

def round_value(
    value,
    digits: int = 2
):
    """
    Round numeric values.
    """

    if pd.isna(value):
        return np.nan

    return round(float(value), digits)


def latest_row(
    data: pd.DataFrame
) -> pd.Series:
    """
    Return latest dataframe row.
    """

    return data.iloc[-1]


# ---------------------------------------------------------
# General Helpers
# ---------------------------------------------------------

def copy_dataframe(
    data: pd.DataFrame
) -> pd.DataFrame:
    """
    Safe dataframe copy.
    """

    return data.copy()


def has_enough_rows(
    data: pd.DataFrame,
    minimum: int
) -> bool:
    """
    Check minimum rows required.
    """

    return len(data) >= minimum


# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

if __name__ == "__main__":

    import yfinance as yf

    df = yf.download(
        "RELIANCE.NS",
        period="3mo",
        progress=False
    )

    validate_ohlcv(df)

    print("Latest Close :", latest_value(df, "Close"))

    print("Previous Close :", previous_value(df, "Close"))

    print("Daily Return :", round(latest_return(df), 2), "%")

    print("Enough Rows :", has_enough_rows(df, 50))
