"""
main.py
======================================
Nifty 50 Momentum Scanner

Project Workflow

1. Load Nifty 50 symbols
2. Download historical data
3. Calculate technical indicators
4. Generate momentum score
5. Rank all stocks
6. Export results to CSV
7. Display Top 10 stocks

Author: Your Name
License: MIT
"""

from pathlib import Path
import pandas as pd

# ---------------------------------------------------------
# Project Modules
# ---------------------------------------------------------

from utils.nifty50 import get_nifty50_symbols

from scanner.downloader import (
    download_stock_data,
)

from scanner.indicators import (
    calculate_indicators,
)

from scanner.scoring import (
    calculate_momentum_score,
)

from scanner.exporter import (
    export_to_csv,
)

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

PERIOD = "6mo"
INTERVAL = "1d"

OUTPUT_FOLDER = Path("output")
OUTPUT_FILE = OUTPUT_FOLDER / "nifty50_momentum.csv"

TOP_RESULTS = 10


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------

def create_output_folder():
    """
    Creates output directory if it does not exist.
    """
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def process_stock(symbol: str):
    """
    Process a single stock.

    Steps
    -----
    1. Download data
    2. Calculate indicators
    3. Calculate momentum score
    4. Return summary dictionary

    Parameters
    ----------
    symbol : str

    Returns
    -------
    dict | None
    """

    print(f"Scanning {symbol}...")

    # ------------------------------------------
    # Download historical data
    # ------------------------------------------

    df = download_stock_data(
        symbol=symbol,
        period=PERIOD,
        interval=INTERVAL,
    )

    # Skip if download failed
    if df is None or df.empty:
        print(f"Skipping {symbol} (No data)")
        return None

    # ------------------------------------------
    # Calculate Indicators
    # ------------------------------------------

    df = calculate_indicators(df)

    # Skip if indicators could not be calculated
    if df is None or df.empty:
        print(f"Skipping {symbol} (Indicator error)")
        return None

    # ------------------------------------------
    # Score stock
    # ------------------------------------------

    result = calculate_momentum_score(
        symbol=symbol,
        df=df,
    )

    return result


def display_top_results(df: pd.DataFrame):
    """
    Prints top ranked stocks.
    """

    print("\n")
    print("=" * 80)
    print("TOP MOMENTUM STOCKS")
    print("=" * 80)

    if df.empty:
        print("No results found.")
        return

    columns = [
        "Rank",
        "Symbol",
        "Score",
        "Close",
        "RSI",
        "EMA20",
        "EMA50",
        "MACD",
        "Volume Breakout",
    ]

    available_columns = [c for c in columns if c in df.columns]

    print(df[available_columns].head(TOP_RESULTS))

    print("=" * 80)


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

def main():

    print("=" * 80)
    print("NIFTY 50 MOMENTUM SCANNER")
    print("=" * 80)

    create_output_folder()

    # ------------------------------------------
    # Load Nifty 50 Symbols
    # ------------------------------------------

    symbols = get_nifty50_symbols()

    print(f"\nLoaded {len(symbols)} symbols.\n")

    results = []

    # ------------------------------------------
    # Scan Every Stock
    # ------------------------------------------

    for symbol in symbols:

        try:

            summary = process_stock(symbol)

            if summary:
                results.append(summary)

        except Exception as e:
            print(f"Error processing {symbol}")
            print(e)

    # ------------------------------------------
    # Convert to DataFrame
    # ------------------------------------------

    if len(results) == 0:
        print("\nNo stocks were processed.")
        return

    rankings = pd.DataFrame(results)

    # ------------------------------------------
    # Rank Stocks
    # ------------------------------------------

    rankings = rankings.sort_values(
        by="Score",
        ascending=False,
    )

    rankings.reset_index(drop=True, inplace=True)

    rankings.insert(
        0,
        "Rank",
        rankings.index + 1,
    )

    # ------------------------------------------
    # Export Results
    # ------------------------------------------

    export_to_csv(
        dataframe=rankings,
        filepath=OUTPUT_FILE,
    )

    # ------------------------------------------
    # Display Results
    # ------------------------------------------

    display_top_results(rankings)

    print(f"\nCSV exported to:\n{OUTPUT_FILE}")

    print("\nScan Complete.")


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
