# Option Chain Dashboard for Indian Stock Traders

A modern Streamlit dashboard for analyzing NSE option chain data.

Built with:

- Python
- Streamlit
- Plotly
- Pandas
- NumPy
- Requests

This project demonstrates how to build a professional options analysis dashboard using publicly available NSE option chain data.

---

## Features

✔ Live Option Chain

✔ PCR (Put Call Ratio)

✔ Max Pain

✔ Open Interest Analysis

✔ Change in Open Interest

✔ ATM Detection

✔ ITM and OTM Identification

✔ Strike Price Table

✔ Interactive Plotly Charts

✔ Expiry Selection

✔ Index Selection

- NIFTY
- BANKNIFTY
- FINNIFTY

---

## Dashboard

Sections include

- Market Summary
- Option Chain Table
- OI Charts
- PCR Gauge
- Max Pain
- IV Table
- Strike Filters
- Greeks (future version)

---

## Technologies

Python

Streamlit

Plotly

Pandas

NumPy

Requests

---

## Installation

Clone repository

```
git clone https://github.com/yourname/option-chain-dashboard.git
```

Move into folder

```
cd option-chain-dashboard
```

Install dependencies

```
pip install -r requirements.txt
```

Run

```
streamlit run app.py
```

---

## Folder Structure

See project tree below.

---

## Roadmap

Version 1

- Live Option Chain
- PCR
- Max Pain
- OI Charts

Version 2

- Greeks
- Strategy Builder
- IV Smile

Version 3

- Backtesting
- Option Screener
- Telegram Alerts

---

## Screens

- Dashboard
- Charts
- Strike Analysis
- Heatmaps

---

## Educational Purpose

This repository accompanies the book

Python for Indian Stock Traders

by Sankar Srinivasan.

The code is intended for educational purposes.

---

option-chain-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── config/
│   ├── settings.py
│   ├── constants.py
│   └── urls.py
│
├── data/
│   ├── nse_api.py
│   ├── fetch_option_chain.py
│   ├── expiry.py
│   └── cache.py
│
├── analysis/
│   ├── pcr.py
│   ├── max_pain.py
│   ├── oi_analysis.py
│   ├── oi_change.py
│   ├── iv.py
│   ├── strikes.py
│   ├── itm_otm.py
│   ├── atm.py
│   └── statistics.py
│
├── charts/
│   ├── oi_chart.py
│   ├── pcr_chart.py
│   ├── max_pain_chart.py
│   ├── iv_chart.py
│   ├── strike_chart.py
│   └── heatmap.py
│
├── dashboard/
│   ├── sidebar.py
│   ├── header.py
│   ├── metrics.py
│   ├── tables.py
│   ├── filters.py
│   └── layout.py
│
├── utils/
│   ├── helpers.py
│   ├── logger.py
│   ├── formatter.py
│   ├── validator.py
│   └── dates.py
│
├── assets/
│   ├── logo.png
│   ├── banner.png
│   └── styles.css
│
├── notebooks/
│   ├── option_chain_demo.ipynb
│   └── pcr_demo.ipynb
│
├── tests/
│   ├── test_pcr.py
│   ├── test_max_pain.py
│   ├── test_atm.py
│   ├── test_iv.py
│   └── test_api.py
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── screenshots.md
│   └── changelog.md
│
└── examples/
    ├── sample_option_chain.csv
    ├── sample_output.csv
    └── sample_dashboard.png
