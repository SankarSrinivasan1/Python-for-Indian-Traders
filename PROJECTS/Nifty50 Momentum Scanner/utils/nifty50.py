"""
nifty50.py
===========

Purpose:
    Stores the list of Nifty 50 stock symbols and provides helper
    functions for retrieving them.

Notes:
    - Yahoo Finance requires Indian stock symbols to end with ".NS".
    - Keep this list updated whenever NSE revises the Nifty 50 index.
    - This module intentionally contains no market download logic.
"""

from typing import List


# ---------------------------------------------------------------------
# NIFTY 50 STOCK SYMBOLS (Yahoo Finance Format)
# ---------------------------------------------------------------------

NIFTY50_SYMBOLS: List[str] = [
    "ADANIENT.NS",
    "ADANIPORTS.NS",
    "APOLLOHOSP.NS",
    "ASIANPAINT.NS",
    "AXISBANK.NS",
    "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS",
    "BAJAJFINSV.NS",
    "BEL.NS",
    "BHARTIARTL.NS",
    "CIPLA.NS",
    "COALINDIA.NS",
    "DRREDDY.NS",
    "EICHERMOT.NS",
    "ETERNAL.NS",          # Previously ZOMATO.NS
    "GRASIM.NS",
    "HCLTECH.NS",
    "HDFCBANK.NS",
    "HDFCLIFE.NS",
    "HEROMOTOCO.NS",
    "HINDALCO.NS",
    "HINDUNILVR.NS",
    "ICICIBANK.NS",
    "INDUSINDBK.NS",
    "INFY.NS",
    "ITC.NS",
    "JIOFIN.NS",
    "JSWSTEEL.NS",
    "KOTAKBANK.NS",
    "LT.NS",
    "M&M.NS",
    "MARUTI.NS",
    "NESTLEIND.NS",
    "NTPC.NS",
    "ONGC.NS",
    "POWERGRID.NS",
    "RELIANCE.NS",
    "SBILIFE.NS",
    "SBIN.NS",
    "SHRIRAMFIN.NS",
    "SUNPHARMA.NS",
    "TATACONSUM.NS",
    "TATAMOTORS.NS",
    "TATASTEEL.NS",
    "TCS.NS",
    "TECHM.NS",
    "TITAN.NS",
    "TRENT.NS",
    "ULTRACEMCO.NS",
    "WIPRO.NS",
]


# ---------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------

def get_nifty50_symbols() -> List[str]:
    """
    Return the complete Nifty 50 symbol list.

    Returns
    -------
    List[str]
        List of Yahoo Finance ticker symbols.
    """
    return NIFTY50_SYMBOLS.copy()


def get_symbol_count() -> int:
    """
    Return the number of stocks in the list.

    Returns
    -------
    int
    """
    return len(NIFTY50_SYMBOLS)


def get_clean_symbol(symbol: str) -> str:
    """
    Convert Yahoo Finance ticker into a cleaner display name.

    Example
    -------
    RELIANCE.NS -> RELIANCE

    Parameters
    ----------
    symbol : str

    Returns
    -------
    str
    """
    return symbol.replace(".NS", "")


def get_display_symbols() -> List[str]:
    """
    Return ticker symbols without the .NS suffix.

    Useful for:
        - Console output
        - CSV reports
        - Dashboards

    Returns
    -------
    List[str]
    """
    return [get_clean_symbol(symbol) for symbol in NIFTY50_SYMBOLS]


def is_valid_symbol(symbol: str) -> bool:
    """
    Check whether a ticker exists in the Nifty 50 list.

    Parameters
    ----------
    symbol : str

    Returns
    -------
    bool
    """
    return symbol.upper() in NIFTY50_SYMBOLS


# ---------------------------------------------------------------------
# Future Enhancement Placeholders
# ---------------------------------------------------------------------

# TODO:
# - Load symbols dynamically from NSE's official constituent list.
# - Cache the downloaded list locally.
# - Support Nifty Next 50.
# - Support Nifty 100.
# - Support Nifty Midcap 100.
# - Support sector-specific indices (Bank Nifty, IT, Pharma, etc.).
# - Add company names alongside ticker symbols.
# - Add sector mapping for sector-wise momentum rankings.
# - Add market-cap classification.
# - Add F&O eligibility flag.
# - Add ESG or thematic tags if required.


# ---------------------------------------------------------------------
# Basic Test
# ---------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 50)
    print("Nifty 50 Stock List")
    print("=" * 50)

    print(f"Total Symbols : {get_symbol_count()}")
    print()

    for index, ticker in enumerate(get_display_symbols(), start=1):
        print(f"{index:02d}. {ticker}")

    print("\nModule loaded successfully.")
