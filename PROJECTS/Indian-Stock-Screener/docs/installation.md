# Installation Guide

## Overview

Indian Stock Screener is a Python application built using Streamlit and pandas-ta for scanning Indian stocks based on popular technical indicators.

This guide explains how to install and run the project on Windows, Linux, and macOS.

---

# Prerequisites

Install the following software before continuing.

- Python 3.11 or later
- Git
- pip

Verify installation.

```bash
python --version
```

```bash
pip --version
```

---

# Clone the Repository

```bash
git clone https://github.com/yourusername/Indian-Stock-Screener.git
```

Move into the project.

```bash
cd Indian-Stock-Screener
```

---

# Create a Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux and macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Verify Installation

Check Streamlit.

```bash
streamlit --version
```

---

# Run the Application

```bash
streamlit run app.py
```

The application opens automatically in your web browser.

Default address

```
http://localhost:8501
```

---

# Required Python Packages

- streamlit
- pandas
- pandas-ta
- numpy
- yfinance
- plotly

---

# Updating Packages

```bash
pip install --upgrade -r requirements.txt
```

---

# Troubleshooting

## Module Not Found

```bash
pip install package_name
```

---

## Streamlit Command Not Found

```bash
python -m streamlit run app.py
```

---

## Virtual Environment Not Activated

Activate the virtual environment before running the application.

---

## Slow Data Download

Internet connection or market data source may be temporarily unavailable.

Retry after a few minutes.

---

# Updating the Repository

```bash
git pull
```

---

# Uninstall

Delete the project folder.

Deactivate virtual environment.

```
deactivate
```

The application has now been completely removed.