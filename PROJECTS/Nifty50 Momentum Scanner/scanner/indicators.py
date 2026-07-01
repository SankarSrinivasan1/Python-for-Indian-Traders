"""
indicators.py
=============

Technical Indicator Engine for the Nifty 50 Momentum Scanner.

Responsibilities
----------------
- Calculate EMA indicators
- Calculate RSI
- Calculate MACD
- Detect EMA crossover
- Detect Volume Breakout
- Return latest indicator values for scoring

This module intentionally keeps indicator calculations isolated from
business logic. Scoring rules belong in scoring.py.

Author: Your Name
Project: Nifty 50 Momentum Scanner
"""

from __future__ import annotations

import pandas as pd
import pandas_ta as ta


# ==========================================================
# Configuration
# ==========================================================

EMA_FAST = 20
EMA_SLOW = 50

RSI_PERIOD = 14

VOLUME_LOOKBACK = 20
VOLUME_BREAKOUT_MULTIPLIER = 1.5


# ==========================================================
# Validation
# ==========================================================

def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Ensure the DataFrame contains all required columns.

    Required Columns
    ----------------
    Open
    High
    Low
    Close
    Volume

    Raises
    ------
    ValueError
        If any required column is missing.
    """

    required_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )


# ==========================================================
# EMA
# ==========================================================

def add_ema(
    df: pd.DataFrame,
    fast: int = EMA_FAST,
    slow: int = EMA_SLOW,
) -> pd.DataFrame:
    """
    Add EMA columns.

    Creates

    EMA_20
    EMA_50

    Returns
    -------
    DataFrame
    """

    validate_dataframe(df)

    df[f"EMA_{fast}"] = ta.ema(
        df["Close"],
        length=fast,
    )

    df[f"EMA_{slow}"] = ta.ema(
        df["Close"],
        length=slow,
    )

    return df


# ==========================================================
# RSI
# ==========================================================

def add_rsi(
    df: pd.DataFrame,
    length: int = RSI_PERIOD,
) -> pd.DataFrame:
    """
    Calculate RSI.

    Creates

    RSI
    """

    validate_dataframe(df)

    df["RSI"] = ta.rsi(
        df["Close"],
        length=length,
    )

    return df


# ==========================================================
# MACD
# ==========================================================

def add_macd(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate MACD.

    Creates

    MACD
    MACD_SIGNAL
    MACD_HIST

    Uses pandas-ta defaults
    """

    validate_dataframe(df)

    macd = ta.macd(df["Close"])

    df["MACD"] = macd.iloc[:, 0]
    df["MACD_SIGNAL"] = macd.iloc[:, 1]
    df["MACD_HIST"] = macd.iloc[:, 2]

    return df


# ==========================================================
# Volume Analysis
# ==========================================================

def add_volume_analysis(
    df: pd.DataFrame,
    lookback: int = VOLUME_LOOKBACK,
    multiplier: float = VOLUME_BREAKOUT_MULTIPLIER,
) -> pd.DataFrame:
    """
    Calculate

    Average Volume

    Volume Ratio

    Volume Breakout
    """

    validate_dataframe(df)

    df["AVG_VOLUME"] = (
        df["Volume"]
        .rolling(lookback)
        .mean()
    )

    df["VOLUME_RATIO"] = (
        df["Volume"]
        / df["AVG_VOLUME"]
    )

    df["VOLUME_BREAKOUT"] = (
        df["VOLUME_RATIO"] >= multiplier
    )

    return df


# ==========================================================
# EMA Crossover
# ==========================================================

def add_ema_crossover(
    df: pd.DataFrame,
    fast: int = EMA_FAST,
    slow: int = EMA_SLOW,
) -> pd.DataFrame:
    """
    Determine whether

    EMA20 > EMA50

    Creates

    EMA_BULLISH
    """

    fast_col = f"EMA_{fast}"
    slow_col = f"EMA_{slow}"

    df["EMA_BULLISH"] = (
        df[fast_col] > df[slow_col]
    )

    return df


# ==========================================================
# Price Above EMA
# ==========================================================

def add_price_position(
    df: pd.DataFrame,
    fast: int = EMA_FAST,
) -> pd.DataFrame:
    """
    Determine whether price is above EMA20.

    Creates

    PRICE_ABOVE_EMA
    """

    ema_col = f"EMA_{fast}"

    df["PRICE_ABOVE_EMA"] = (
        df["Close"] > df[ema_col]
    )

    return df


# ==========================================================
# MACD Bullish
# ==========================================================

def add_macd_signal(df: pd.DataFrame) -> pd.DataFrame:
    """
    Determine MACD bullishness.

    Creates

    MACD_BULLISH
    """

    df["MACD_BULLISH"] = (
        df["MACD"] > df["MACD_SIGNAL"]
    )

    return df


# ==========================================================
# Price Momentum
# ==========================================================

def add_price_momentum(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simple one-day momentum.

    Creates

    PRICE_UP
    """

    df["PRICE_UP"] = (
        df["Close"] > df["Close"].shift(1)
    )

    return df


# ==========================================================
# Master Function
# ==========================================================

def calculate_all_indicators(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Execute every indicator calculation.

    Processing Order

    1. EMA

    2. RSI

    3. MACD

    4. Volume

    5. EMA crossover

    6. Price above EMA

    7. MACD bullish

    8. Price momentum
    """

    validate_dataframe(df)

    df = add_ema(df)
    df = add_rsi(df)
    df = add_macd(df)

    df = add_volume_analysis(df)

    df = add_ema_crossover(df)

    df = add_price_position(df)

    df = add_macd_signal(df)

    df = add_price_momentum(df)

    return df


# ==========================================================
# Latest Snapshot
# ==========================================================

def latest_values(
    df: pd.DataFrame,
) -> dict:
    """
    Return the latest row as a dictionary.

    This is useful for scoring.py.

    Returns
    -------
    dict
    """

    latest = df.iloc[-1]

    return {
        "close": latest["Close"],
        "ema20": latest["EMA_20"],
        "ema50": latest["EMA_50"],
        "price_above_ema": latest["PRICE_ABOVE_EMA"],
        "ema_bullish": latest["EMA_BULLISH"],
        "rsi": latest["RSI"],
        "macd": latest["MACD"],
        "macd_signal": latest["MACD_SIGNAL"],
        "macd_bullish": latest["MACD_BULLISH"],
        "volume": latest["Volume"],
        "avg_volume": latest["AVG_VOLUME"],
        "volume_breakout": latest["VOLUME_BREAKOUT"],
        "price_up": latest["PRICE_UP"],
    }


# ==========================================================
# Future Enhancements (Placeholders)
# ==========================================================
#
# TODO:
# - Supertrend
# - ATR
# - ADX
# - Bollinger Bands
# - VWAP
# - Stochastic RSI
# - Relative Strength vs Nifty 50
# - 52 Week High/Low
# - Support & Resistance
# - Candlestick Pattern Detection
# - Multi-timeframe indicator calculations
#
# ==========================================================
