"""
logger.py

Central logging utility for the Indian Stock Screener.
"""

import logging
import os

from utils.constants import (
    LOG_FOLDER,
    LOG_FILE,
    LOG_LEVEL,
)


def create_log_directory():
    """
    Create the log directory if it does not exist.
    """

    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)


def get_logger(name: str = "IndianStockScreener"):
    """
    Returns a configured logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
    """

    create_log_directory()

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)

    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    log_path = os.path.join(LOG_FOLDER, LOG_FILE)

    file_handler = logging.FileHandler(
        log_path,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


# ---------------------------------------------------
# Default application logger
# ---------------------------------------------------

logger = get_logger()


# ---------------------------------------------------
# Convenience Functions
# ---------------------------------------------------

def log_info(message: str):
    logger.info(message)


def log_warning(message: str):
    logger.warning(message)


def log_error(message: str):
    logger.error(message)


def log_debug(message: str):
    logger.debug(message)


def log_exception(message: str):
    """
    Logs an exception with traceback.
    """
    logger.exception(message)
