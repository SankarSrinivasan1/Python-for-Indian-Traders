"""
Application Settings

Project:
Option Chain Dashboard

Author:
Sankar Srinivasan
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------

APP_NAME = "Option Chain Dashboard"
APP_VERSION = "1.0.0"

# -----------------------------------------------------------------------------
# Directories
# -----------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
CACHE_DIR = BASE_DIR / "cache"
LOG_DIR = BASE_DIR / "logs"

CACHE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# -----------------------------------------------------------------------------
# Dashboard
# -----------------------------------------------------------------------------

DEFAULT_INDEX = "NIFTY"

AVAILABLE_INDICES = [
    "NIFTY",
    "BANKNIFTY",
    "FINNIFTY",
]

DEFAULT_REFRESH_INTERVAL = 60  # seconds

# -----------------------------------------------------------------------------
# Plotly
# -----------------------------------------------------------------------------

PLOT_HEIGHT = 500
PLOT_WIDTH = 900

# -----------------------------------------------------------------------------
# Streamlit
# -----------------------------------------------------------------------------

PAGE_TITLE = APP_NAME
PAGE_ICON = "📈"
LAYOUT = "wide"

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

REQUEST_TIMEOUT = 15

ENABLE_CACHE = True

CACHE_EXPIRY = 60

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FILE = LOG_DIR / "dashboard.log"
