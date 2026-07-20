# data/nse_api.py

## Overview

`nse_api.py` is the foundation of the Option Chain Dashboard. It provides a simple, reusable interface for communicating with the NSE India Option Chain API while handling session management and HTTP requests behind the scenes.

The module is designed to be lightweight, reliable, and easy to extend. Other modules in the project use this class instead of making direct API calls.

---

## Responsibilities

The `NSEAPI` class handles:

- Establishing an HTTP session with NSE India
- Managing request headers
- Initializing cookies required by the NSE website
- Refreshing expired sessions automatically
- Downloading live option chain data
- Providing helper methods for commonly used information

---

## Features

- Persistent `requests.Session` for improved performance
- Automatic cookie initialization
- Automatic session refresh on HTTP 401 responses
- Configurable market symbols
  - NIFTY
  - BANKNIFTY
  - FINNIFTY
- Returns raw option chain JSON from NSE
- Clean, object-oriented API
- Type hints for improved readability
- Comprehensive inline documentation
- Standalone test block for quick verification

---

## Class

```
NSEAPI
```

Main class responsible for communicating with the NSE Option Chain API.

---

## Methods

### initialize_session()

Creates an HTTP session and retrieves the cookies required by the NSE website.

---

### refresh_session()

Clears existing cookies and creates a fresh session when authentication expires.

---

### fetch_option_chain(symbol)

Downloads the complete option chain JSON for the selected index.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| symbol | str | NIFTY, BANKNIFTY or FINNIFTY |

**Returns**

```
dict
```

Raw JSON response from the NSE API.

---

### get_records(symbol)

Returns only the option chain records from the JSON response.

**Returns**

```
list
```

---

### get_expiry_dates(symbol)

Returns all available expiry dates.

**Returns**

```
list
```

---

### get_underlying_value(symbol)

Returns the current underlying index value.

**Returns**

```
float
```

---

## Supported Symbols

- NIFTY
- BANKNIFTY
- FINNIFTY

Additional symbols can be added with minimal changes.

---

## Why Use requests.Session?

Using a persistent session provides several advantages:

- Reuses TCP connections
- Maintains cookies automatically
- Faster than creating a new connection for every request
- Better compatibility with NSE's security mechanisms

---

## Session Management

The module automatically:

1. Opens the NSE homepage.
2. Retrieves authentication cookies.
3. Stores cookies in the session.
4. Reuses the session for future requests.
5. Refreshes the session automatically if a 401 Unauthorized response is received.

No manual cookie management is required.

---

## Example

```python
from data.nse_api import NSEAPI

api = NSEAPI()

data = api.fetch_option_chain("NIFTY")

print(api.get_underlying_value())

print(api.get_expiry_dates())

records = api.get_records()

print(len(records))
```

---

## Dependencies

- requests
- typing

---

## Error Handling

The module raises descriptive exceptions when:

- Network connectivity fails
- The NSE website is unavailable
- Invalid HTTP responses are received
- Session initialization fails

---

## Design Goals

- Simple API
- Modular architecture
- Reusable across projects
- Easy to maintain
- Beginner-friendly
- Production-ready foundation

---

## Next Module

The next component in the project is:

```
data/fetch_option_chain.py
```

This module builds on `nse_api.py` by converting the raw NSE option chain JSON into a clean, structured Pandas DataFrame suitable for analysis, visualization, and dashboard development.
