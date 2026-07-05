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
