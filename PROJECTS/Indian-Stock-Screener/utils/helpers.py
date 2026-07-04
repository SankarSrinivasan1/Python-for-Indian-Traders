"""
helpers.py

Common helper functions used across the application.
"""

from datetime import datetime


def round_price(value: float, decimals: int = 2) -> float:
    """
    Round a price to the specified decimal places.

    Parameters
    ----------
    value : float
        Price value.

    decimals : int
        Number of decimal places.

    Returns
    -------
    float
    """
    try:
        return round(float(value), decimals)
    except (TypeError, ValueError):
        return 0.0


def calculate_percentage_change(current: float, previous: float) -> float:
    """
    Calculate percentage price change.
    """

    try:
        if previous == 0:
            return 0.0

        return ((current - previous) / previous) * 100

    except Exception:
        return 0.0


def calculate_price_change(current: float, previous: float) -> float:
    """
    Calculate absolute price change.
    """

    try:
        return current - previous
    except Exception:
        return 0.0


def is_above(price: float, level: float) -> bool:
    """
    Returns True if price is above a level.
    """

    return price > level


def is_below(price: float, level: float) -> bool:
    """
    Returns True if price is below a level.
    """

    return price < level


def get_current_timestamp() -> str:
    """
    Returns current timestamp.

    Example
    -------
    2026-07-04 14:25:36
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_symbol(symbol: str) -> str:
    """
    Clean stock symbol.
    """

    return symbol.strip().upper()


def safe_float(value, default=0.0):
    """
    Safely convert to float.
    """

    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def safe_int(value, default=0):
    """
    Safely convert to integer.
    """

    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def percentage_string(value: float) -> str:
    """
    Convert percentage to readable string.

    Example
    -------
    4.58%
    """

    return f"{value:.2f}%"
