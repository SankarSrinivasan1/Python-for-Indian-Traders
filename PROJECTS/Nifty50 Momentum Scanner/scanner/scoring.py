"""
scoring.py
===========

Purpose
-------
Calculate a momentum score for each stock based on technical indicators
and rank all scanned stocks.

This module contains ONLY the scoring logic.

Expected Input
--------------
A pandas DataFrame containing the latest indicator values for one stock.

Expected Columns
----------------
Close
EMA20
EMA50
RSI
MACD
MACD_SIGNAL
Volume
AVG_VOLUME20

(Optional future columns)

ADX
SUPERTREND
ATR
52W_HIGH
52W_LOW

Output
------
Dictionary containing:

{
    "Score": 85,
    "Reasons": [
        "Price above EMA20",
        "EMA20 above EMA50",
        "Bullish MACD"
    ]
}

Educational Project
Python for Indian Stock Traders
"""

from typing import Dict, List
import pandas as pd


# ==========================================================
# Configuration
# ==========================================================

MAX_SCORE = 100

# Individual rule weights.
# Feel free to customize these values.
WEIGHTS = {
    "price_above_ema20": 20,
    "ema_crossover": 20,
    "rsi_strength": 15,
    "macd_bullish": 20,
    "volume_breakout": 15,
    "price_up_today": 10,
}


# ==========================================================
# Helper Functions
# ==========================================================

def is_price_above_ema20(row: pd.Series) -> bool:
    """
    Returns True if Close > EMA20.
    """

    return row["Close"] > row["EMA20"]


def is_ema_bullish(row: pd.Series) -> bool:
    """
    Bullish EMA crossover.

    EMA20 > EMA50
    """

    return row["EMA20"] > row["EMA50"]


def is_rsi_strong(row: pd.Series) -> bool:
    """
    Returns True if RSI is within
    the preferred bullish zone.

    Default:
    50 <= RSI <= 70

    You may modify these values later.
    """

    return 50 <= row["RSI"] <= 70


def is_macd_bullish(row: pd.Series) -> bool:
    """
    Bullish MACD crossover.

    MACD > Signal
    """

    return row["MACD"] > row["MACD_SIGNAL"]


def is_volume_breakout(row: pd.Series) -> bool:
    """
    Volume breakout rule.

    Default:
    Current Volume >
    1.5 x 20-day Average Volume
    """

    return row["Volume"] > (1.5 * row["AVG_VOLUME20"])


def is_price_up_today(row: pd.Series) -> bool:
    """
    Today's close greater than previous close.

    Expected column:
    PREV_CLOSE

    Placeholder until previous day's close
    is added by the indicator module.
    """

    if "PREV_CLOSE" not in row:
        return False

    return row["Close"] > row["PREV_CLOSE"]


# ==========================================================
# Core Scoring Logic
# ==========================================================

def score_stock(row: pd.Series) -> Dict:
    """
    Calculate momentum score for a single stock.

    Parameters
    ----------
    row : pandas.Series

    Returns
    -------
    dict
    """

    score = 0
    reasons: List[str] = []

    # ----------------------------------------------
    # Rule 1
    # ----------------------------------------------

    if is_price_above_ema20(row):
        score += WEIGHTS["price_above_ema20"]
        reasons.append("Price above EMA20")

    # ----------------------------------------------
    # Rule 2
    # ----------------------------------------------

    if is_ema_bullish(row):
        score += WEIGHTS["ema_crossover"]
        reasons.append("EMA20 above EMA50")

    # ----------------------------------------------
    # Rule 3
    # ----------------------------------------------

    if is_rsi_strong(row):
        score += WEIGHTS["rsi_strength"]
        reasons.append("Healthy RSI")

    # ----------------------------------------------
    # Rule 4
    # ----------------------------------------------

    if is_macd_bullish(row):
        score += WEIGHTS["macd_bullish"]
        reasons.append("Bullish MACD")

    # ----------------------------------------------
    # Rule 5
    # ----------------------------------------------

    if is_volume_breakout(row):
        score += WEIGHTS["volume_breakout"]
        reasons.append("Volume Breakout")

    # ----------------------------------------------
    # Rule 6
    # ----------------------------------------------

    if is_price_up_today(row):
        score += WEIGHTS["price_up_today"]
        reasons.append("Price Up Today")

    score = min(score, MAX_SCORE)

    return {
        "Score": score,
        "Reasons": reasons
    }


# ==========================================================
# Ranking Engine
# ==========================================================

def rank_stocks(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply scoring to every stock.

    Expected input:
    One row per stock.

    Returns
    -------
    Ranked DataFrame
    """

    results = []

    for _, row in df.iterrows():

        result = score_stock(row)

        stock = row.to_dict()

        stock["Score"] = result["Score"]

        stock["Reasons"] = ", ".join(result["Reasons"])

        results.append(stock)

    ranked = pd.DataFrame(results)

    ranked = ranked.sort_values(
        by="Score",
        ascending=False
    ).reset_index(drop=True)

    ranked.insert(
        0,
        "Rank",
        range(1, len(ranked) + 1)
    )

    return ranked


# ==========================================================
# Future Enhancements
# ==========================================================

"""
Ideas for Version 2

□ Relative Strength Ranking
□ ATR Trend Score
□ ADX Trend Strength
□ Supertrend Confirmation
□ Multi-Timeframe Confirmation
□ Sector Relative Strength
□ Breakout Above 52-Week High
□ VWAP Confirmation
□ Institutional Volume Filter
□ Machine Learning Score
□ AI Confidence Score
□ Dynamic Rule Weighting
□ Configurable Rules from JSON
□ User-defined Scoring Templates
"""


# ==========================================================
# Example Usage
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Momentum Scoring Module")
    print("=" * 60)

    print("\nThis module is intended to be imported by main.py")
    print("Use rank_stocks(dataframe) after indicators are calculated.")
