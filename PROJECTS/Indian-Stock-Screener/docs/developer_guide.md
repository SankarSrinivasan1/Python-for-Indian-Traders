# Developer Guide

## Overview

This document explains the internal architecture of the Indian Stock Screener project and how to extend it by adding new indicators, screeners, and data sources.

The project follows a modular structure to keep the code clean, reusable, and easy to maintain.

---

# Project Architecture

```
User Interface
        │
        ▼
Streamlit Dashboard
        │
        ▼
Screener Manager
        │
        ├──────────────┐
        ▼              ▼
Technical       Market Data
Indicators        Downloader
        │              │
        └──────┬───────┘
               ▼
        Results Table
               │
               ▼
          CSV Export
```

---

# Main Components

## app.py

Application entry point.

Responsibilities

- Launch Streamlit
- Load sidebar
- Accept user inputs
- Execute selected screener
- Display results

---

## data_source/

Responsible for downloading market data.

Example modules

- yahoo_data.py
- nse_data.py
- downloader.py

---

## indicators/

Contains reusable technical indicators.

Example

```
rsi.py
ema.py
adx.py
bollinger.py
supertrend.py
```

Each file should expose a single function.

Example

```python
calculate_rsi(data)
```

---

## screeners/

Contains trading strategies.

Each screener should

- Receive stock data
- Calculate indicators
- Return True or False

Example

```python
is_rsi_oversold()
```

---

## ui/

Contains Streamlit user interface components.

Examples

- Sidebar
- Dashboard
- Filters
- Results table

---

## utils/

Contains helper functions.

Examples

- CSV export
- Logging
- Validation
- Formatting

---

# Adding a New Screener

Step 1

Create a new file inside

```
screeners/
```

Example

```
macd_crossover.py
```

Step 2

Implement screening logic.

Step 3

Register the screener inside

```
screener_manager.py
```

Step 4

Add the option to the Streamlit sidebar.

---

# Coding Standards

- Follow PEP 8
- Use descriptive variable names
- Write reusable functions
- Keep functions small
- Add docstrings
- Avoid duplicated code

---

# Testing

Run unit tests

```bash
pytest
```

---

# Suggested Future Modules

- MACD
- VWAP
- Ichimoku Cloud
- ATR
- Relative Strength
- Fibonacci Scanner
- Pivot Points
- Delivery Volume
- Open Interest Analysis

---

# Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Push the branch.
5. Submit a Pull Request.

Happy coding!
