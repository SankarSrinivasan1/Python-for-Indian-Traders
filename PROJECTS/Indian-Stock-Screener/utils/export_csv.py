"""
export_csv.py

Utility functions to export screening results to CSV.
"""

from pathlib import Path
from datetime import datetime

import pandas as pd

from utils.constants import (
    EXPORT_FOLDER,
    CSV_FILE_PREFIX,
)

from utils.logger import logger


def create_export_directory() -> Path:
    """
    Create the export directory if it does not exist.

    Returns
    -------
    Path
        Path object for the export directory.
    """

    export_path = Path(EXPORT_FOLDER)
    export_path.mkdir(parents=True, exist_ok=True)

    return export_path


def generate_filename(prefix: str = CSV_FILE_PREFIX) -> str:
    """
    Generate a timestamped filename.

    Example:
    screening_results_20260705_093015.csv
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.csv"


def export_dataframe(
    dataframe: pd.DataFrame,
    filename: str | None = None,
    index: bool = False,
) -> str:
    """
    Export a DataFrame to CSV.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Data to export.

    filename : str, optional
        Custom filename.

    index : bool
        Include DataFrame index.

    Returns
    -------
    str
        Full path of exported CSV file.
    """

    if dataframe is None or dataframe.empty:
        raise ValueError("Nothing to export. DataFrame is empty.")

    export_dir = create_export_directory()

    if filename is None:
        filename = generate_filename()

    file_path = export_dir / filename

    dataframe.to_csv(
        file_path,
        index=index,
        encoding="utf-8-sig"
    )

    logger.info(f"CSV exported successfully: {file_path}")

    return str(file_path)


def export_selected_columns(
    dataframe: pd.DataFrame,
    columns: list,
    filename: str | None = None,
) -> str:
    """
    Export only selected columns.
    """

    if dataframe is None or dataframe.empty:
        raise ValueError("DataFrame is empty.")

    export_df = dataframe[columns]

    return export_dataframe(
        export_df,
        filename=filename,
        index=False
    )


def export_watchlist(
    symbols: list,
    filename: str = "watchlist.csv",
) -> str:
    """
    Export a watchlist to CSV.
    """

    df = pd.DataFrame({
        "Symbol": symbols
    })

    return export_dataframe(
        df,
        filename=filename,
        index=False
    )


def save_scan_results(
    dataframe: pd.DataFrame,
) -> str:
    """
    Save screening results using the default naming convention.
    """

    return export_dataframe(dataframe)


def export_summary(
    dataframe: pd.DataFrame,
) -> dict:
    """
    Return summary statistics for the exported data.
    """

    return {
        "rows": len(dataframe),
        "columns": len(dataframe.columns),
        "column_names": list(dataframe.columns),
  }
