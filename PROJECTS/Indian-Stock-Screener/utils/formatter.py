"""
formatter.py

Formatting utilities for the Indian Stock Screener.
"""

from datetime import datetime


def format_price(price: float, decimals: int = 2) -> str:
    """
    Format a price with comma separators.

    Example:
    123456.789 -> 123,456.79
    """

    try:
        return f"{float(price):,.{decimals}f}"
    except (TypeError, ValueError):
        return "0.00"


def format_percentage(value: float, decimals: int = 2) -> str:
    """
    Format a percentage.

    Example:
    4.5678 -> 4.57%
    """

    try:
        return f"{float(value):.{decimals}f}%"
    except (TypeError, ValueError):
        return "0.00%"


def format_volume(volume: float) -> str:
    """
    Convert large numbers into readable format.

    Examples
    --------
    1250       -> 1.25 K
    1540000    -> 1.54 M
    250000000  -> 250.00 M
    """

    try:
        volume = float(volume)

        if volume >= 1_000_000_000:
            return f"{volume / 1_000_000_000:.2f} B"

        if volume >= 1_000_000:
            return f"{volume / 1_000_000:.2f} M"

        if volume >= 1_000:
            return f"{volume / 1_000:.2f} K"

        return str(int(volume))

    except (TypeError, ValueError):
        return "0"


def format_currency(value: float, symbol: str = "₹") -> str:
    """
    Format Indian currency.

    Example:
    ₹1,234.56
    """

    try:
        return f"{symbol}{float(value):,.2f}"
    except (TypeError, ValueError):
        return f"{symbol}0.00"


def format_date(date_value) -> str:
    """
    Convert datetime/date into YYYY-MM-DD format.
    """

    try:
        if isinstance(date_value, datetime):
            return date_value.strftime("%Y-%m-%d")

        return str(date_value)

    except Exception:
        return ""


def format_datetime(date_value) -> str:
    """
    Convert datetime into readable format.

    Example:
    2026-07-05 09:30:00
    """

    try:
        if isinstance(date_value, datetime):
            return date_value.strftime("%Y-%m-%d %H:%M:%S")

        return str(date_value)

    except Exception:
        return ""


def format_signal(signal: str) -> str:
    """
    Normalize trading signals.
    """

    if signal is None:
        return "N/A"

    signal = signal.strip().upper()

    mapping = {
        "BUY": "🟢 BUY",
        "SELL": "🔴 SELL",
        "HOLD": "🟡 HOLD",
        "NEUTRAL": "⚪ NEUTRAL"
    }

    return mapping.get(signal, signal)


def format_boolean(value: bool) -> str:
    """
    Convert boolean to Yes/No.
    """

    return "Yes" if value else "No"


def format_dataframe_columns(df):
    """
    Standardize DataFrame column names.

    Example:
    close_price -> Close Price
    """

    df.columns = [
        column.replace("_", " ").title()
        for column in df.columns
    ]

    return df
