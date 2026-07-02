"""
settings.py
============

Central configuration file for the Nifty 50 Momentum Scanner.

Modify values here to customize the scanner without changing the
application code.

Author: Your Name
Project: Nifty 50 Momentum Scanner
"""

from pathlib import Path

# =============================================================================
# PROJECT PATHS
# =============================================================================

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Folder to optionally store downloaded market data
DATA_DIR = BASE_DIR / "data"

# Folder where scan results will be exported
OUTPUT_DIR = BASE_DIR / "output"

# Ensure required folders exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =============================================================================
# MARKET DATA SETTINGS
# =============================================================================

# Yahoo Finance period
# Examples:
# 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y
DEFAULT_PERIOD = "6mo"

# Candle interval
# Examples:
# 1d, 1wk, 1mo
DEFAULT_INTERVAL = "1d"

# =============================================================================
# TECHNICAL INDICATOR SETTINGS
# =============================================================================

# Exponential Moving Averages
EMA_FAST = 20
EMA_SLOW = 50

# RSI
RSI_LENGTH = 14

# MACD
MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

# Volume breakout settings
VOLUME_AVERAGE_PERIOD = 20
VOLUME_BREAKOUT_MULTIPLIER = 1.5

# =============================================================================
# MOMENTUM SCORING
# =============================================================================

# Maximum possible score
MAX_SCORE = 100

# Individual rule weights
SCORE_PRICE_ABOVE_EMA20 = 20
SCORE_EMA_CROSSOVER = 20
SCORE_RSI_BULLISH = 15
SCORE_MACD_BULLISH = 20
SCORE_VOLUME_BREAKOUT = 15
SCORE_PRICE_UP_TODAY = 10

# =============================================================================
# RSI CONDITIONS
# =============================================================================

RSI_BULLISH_MIN = 50
RSI_BULLISH_MAX = 70

# =============================================================================
# EXPORT SETTINGS
# =============================================================================

EXPORT_FILENAME = "nifty50_momentum.csv"

EXPORT_FULL_PATH = OUTPUT_DIR / EXPORT_FILENAME

EXPORT_INDEX = False

# =============================================================================
# DISPLAY SETTINGS
# =============================================================================

# Number of stocks shown in terminal
TOP_RESULTS = 10

# Sort results by momentum score
SORT_DESCENDING = True

# Decimal precision while printing
ROUND_DECIMALS = 2

# =============================================================================
# DOWNLOAD SETTINGS
# =============================================================================

# Delay (seconds) between requests if required
REQUEST_DELAY = 0.2

# Retry attempts for failed downloads
MAX_RETRIES = 3

# =============================================================================
# OPTIONAL FEATURES (Future Versions)
# =============================================================================

ENABLE_CACHE = False

CACHE_FOLDER = DATA_DIR / "cache"

ENABLE_LOGGING = True

LOG_FILE = BASE_DIR / "scanner.log"

ENABLE_TELEGRAM_ALERTS = False

ENABLE_EMAIL_ALERTS = False

ENABLE_STREAMLIT = False

# =============================================================================
# DEBUG
# =============================================================================

DEBUG = False

# =============================================================================
# END OF CONFIGURATION
# =============================================================================
