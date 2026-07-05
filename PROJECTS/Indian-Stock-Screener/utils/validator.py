"""
validator.py

Validation functions for the Indian Stock Screener.
"""

from typing import Any
import pandas as pd


def is_dataframe_valid(df: pd.DataFrame) -> bool:
    """
    Check whether a DataFrame exists and contains data.
    """

    return df is not None and not df.empty


def has_required_columns(
    df: pd.DataFrame,
    required_columns: list
) -> bool:
    """
    Verify all required columns exist.
    """

    if not is_dataframe_valid(df):
        return False

    return all(column in df.columns for column in required_columns)


def validate_symbol(symbol: str) -> bool:
    """
    Validate stock symbol.
    """

    if symbol is None:
        return False

    symbol = symbol.strip()

    if symbol == "":
        return False

    if len(symbol) < 2:
        return False

    return True


def validate_positive_number(value: Any) -> bool:
    """
    Check whether value is a positive number.
    """

    try:
        return float(value) > 0
    except (TypeError, ValueError):
        return False


def validate_non_negative_number(value: Any) -> bool:
    """
    Check whether value is zero or greater.
    """

    try:
        return float(value) >= 0
    except (TypeError, ValueError):
        return False


def validate_rsi(value: float) -> bool:
    """
    RSI must be between 0 and 100.
    """

    try:
        value = float(value)
        return 0 <= value <= 100
    except (TypeError, ValueError):
        return False


def validate_adx(value: float) -> bool:
    """
    ADX cannot be negative.
    """

    try:
        value = float(value)
        return value >= 0
    except (TypeError, ValueError):
        return False


def validate_period(period: int) -> bool:
    """
    Validate indicator period.
    """

    try:
        period = int(period)
        return period > 0
    except (TypeError, ValueError):
        return False


def validate_screening_result(df: pd.DataFrame) -> bool:
    """
    Validate screening results before display/export.
    """

    if not is_dataframe_valid(df):
        return False

    required = [
        "Symbol",
        "Close"
    ]

    return has_required_columns(df, required)


def validate_export_path(path: str) -> bool:
    """
    Validate export file path.
    """

    if path is None:
        return False

    return len(path.strip()) > 0


def validate_strategy(strategy: str, available: list) -> bool:
    """
    Check whether selected strategy exists.
    """

    if strategy is None:
        return False

    return strategy in available


def validate_watchlist(symbols: list) -> bool:
    """
    Validate watchlist.
    """

    if not isinstance(symbols, list):
        return False

    if len(symbols) == 0:
        return False

    return all(validate_symbol(symbol) for symbol in symbols)


def validate_dataframe_not_empty(df: pd.DataFrame):
    """
    Raise an exception if DataFrame is empty.
    """

    if df is None or df.empty:
        raise ValueError("No market data available.")
