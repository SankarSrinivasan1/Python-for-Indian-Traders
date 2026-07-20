"""
NSE API URLs

Note:
The NSE website may change its endpoints or require session cookies.
Always create a session before requesting data.
"""

# -----------------------------------------------------------------------------
# Base URL
# -----------------------------------------------------------------------------

BASE_URL = "https://www.nseindia.com"

# -----------------------------------------------------------------------------
# Landing Page
# -----------------------------------------------------------------------------

HOME_PAGE = f"{BASE_URL}"

# -----------------------------------------------------------------------------
# Option Chain APIs
# -----------------------------------------------------------------------------

OPTION_CHAIN_INDICES = (
    f"{BASE_URL}/api/option-chain-indices"
)

OPTION_CHAIN_EQUITIES = (
    f"{BASE_URL}/api/option-chain-equities"
)

# -----------------------------------------------------------------------------
# Quote APIs
# -----------------------------------------------------------------------------

QUOTE_EQUITY = (
    f"{BASE_URL}/api/quote-equity"
)

QUOTE_DERIVATIVE = (
    f"{BASE_URL}/api/quote-derivative"
)

# -----------------------------------------------------------------------------
# Market Status
# -----------------------------------------------------------------------------

MARKET_STATUS = (
    f"{BASE_URL}/api/marketStatus"
)

# -----------------------------------------------------------------------------
# Holiday Calendar
# -----------------------------------------------------------------------------

HOLIDAY_MASTER = (
    f"{BASE_URL}/api/holiday-master"
)

# -----------------------------------------------------------------------------
# HTTP Headers
# -----------------------------------------------------------------------------

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": BASE_URL,
    "Connection": "keep-alive",
}

# -----------------------------------------------------------------------------
# Default Parameters
# -----------------------------------------------------------------------------

DEFAULT_SYMBOL = "NIFTY"

DEFAULT_TIMEOUT = 15
