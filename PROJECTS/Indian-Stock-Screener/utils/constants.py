"""
constants.py

Application-wide constants for the Indian Stock Screener.
"""

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "Indian Stock Screener"
APP_VERSION = "1.0.0"

AUTHOR = "Sankar Srinivasan"

# ==========================================================
# Default Technical Indicator Values
# ==========================================================

DEFAULT_RSI_PERIOD = 14

DEFAULT_SHORT_EMA = 50
DEFAULT_LONG_EMA = 200

DEFAULT_ADX_PERIOD = 14
DEFAULT_ADX_THRESHOLD = 25

DEFAULT_SUPERTREND_LENGTH = 10
DEFAULT_SUPERTREND_MULTIPLIER = 3

DEFAULT_BB_LENGTH = 20
DEFAULT_BB_STD = 2

# ==========================================================
# Market Data
# ==========================================================

DEFAULT_LOOKBACK_DAYS = 365

MIN_REQUIRED_CANDLES = 250

DEFAULT_INTERVAL = "1d"

# ==========================================================
# Supported Screeners
# ==========================================================

SCREENERS = [
    "RSI Oversold",
    "RSI Overbought",
    "Golden Cross",
    "Supertrend Buy",
    "ADX Strong Trend",
    "Bollinger Breakout",
]

# ==========================================================
# Export
# ==========================================================

EXPORT_FOLDER = "reports/exports"

CSV_FILE_PREFIX = "screening_results"

# ==========================================================
# Streamlit
# ==========================================================

PAGE_TITLE = "Indian Stock Screener"

PAGE_ICON = "📈"

LAYOUT = "wide"

# ==========================================================
# Colors
# ==========================================================

BUY_COLOR = "#16A34A"

SELL_COLOR = "#DC2626"

NEUTRAL_COLOR = "#2563EB"

WARNING_COLOR = "#F59E0B"

# ==========================================================
# Column Names
# ==========================================================

COLUMN_SYMBOL = "Symbol"

COLUMN_CLOSE = "Close"

COLUMN_VOLUME = "Volume"

COLUMN_RSI = "RSI"

COLUMN_ADX = "ADX"

COLUMN_SIGNAL = "Signal"

COLUMN_DATE = "Date"

# ==========================================================
# Logging
# ==========================================================

LOG_FOLDER = "logs"

LOG_FILE = "screener.log"

LOG_LEVEL = "INFO"

# ==========================================================
# Miscellaneous
# ==========================================================

DATE_FORMAT = "%Y-%m-%d"

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

DECIMAL_PLACES = 2
