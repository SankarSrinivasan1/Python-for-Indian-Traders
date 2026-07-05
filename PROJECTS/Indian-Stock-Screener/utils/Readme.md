## Example Usage of logger.py

### Using the Default Logger

```python
from utils.logger import logger

logger.info("Application started.")

logger.warning("Yahoo Finance is temporarily unavailable.")

logger.error("Unable to download data.")
```

---

### Using Helper Functions

```python
from utils.logger import log_info

log_info("Running RSI Screener...")
```

You can also use the other helper functions:

```python
from utils.logger import (
    log_info,
    log_warning,
    log_error,
    log_debug,
    log_exception,
)

log_info("Application started.")
log_warning("Market data source is slow.")
log_error("Failed to download stock data.")
log_debug("Scanning NIFTY 50 stocks...")
```

---

## Features

- ✅ Automatically creates the `logs/` folder if it doesn't exist.
- ✅ Writes log messages to both the console and a log file.
- ✅ Prevents duplicate log entries by avoiding multiple handlers.
- ✅ Includes timestamps, log levels, and logger names in every log message.
- ✅ Provides simple helper functions like `log_info()`, `log_warning()`, `log_error()`, `log_debug()`, and `log_exception()`.
- ✅ Suitable for both development and production environments.

---

## Example Usage of formatter.py

```python
from utils.formatter import (
    format_price,
    format_percentage,
    format_volume,
    format_signal,
)

print(format_price(2543.756))
# Output: 2,543.76

print(format_percentage(4.2356))
# Output: 4.24%

print(format_volume(2356000))
# Output: 2.36 M

print(format_signal("buy"))
# Output: 🟢 BUY
```

---

## Features

- ✅ Formats prices with comma separators.
- ✅ Formats percentages consistently.
- ✅ Converts large volume values into **K**, **M**, and **B** notation.
- ✅ Formats currency using the **₹ (Indian Rupee)** symbol by default.
- ✅ Formats dates and timestamps into readable formats.
- ✅ Displays trading signals with intuitive icons.
- ✅ Standardizes pandas DataFrame column names for consistent presentation.

---

# Validator Module

The `validator.py` module provides reusable validation functions for the **Indian Stock Screener**. It helps ensure that user inputs, market data, and screening parameters are valid before processing.

---

## Example Usage

```python
from utils.validator import (
    validate_symbol,
    validate_rsi,
    validate_strategy,
)

print(validate_symbol("RELIANCE"))
# True

print(validate_rsi(75))
# True

print(validate_rsi(120))
# False
```

---

## Validation Features

The module validates the following:

- ✅ Stock symbols
- ✅ DataFrames
- ✅ Required DataFrame columns
- ✅ RSI values (0–100)
- ✅ ADX values
- ✅ Indicator periods
- ✅ Strategy names
- ✅ Watchlists
- ✅ Export file paths
- ✅ Screening results

---

## Benefits

- Prevents invalid user input
- Reduces runtime errors
- Improves application reliability
- Centralizes validation logic
- Makes the codebase easier to maintain and extend
