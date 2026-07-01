# Nifty 50 Momentum Scanner

A Python-based stock momentum scanner for Indian stock traders.

This project downloads historical data for all Nifty 50 stocks, calculates popular technical indicators, scores each stock based on bullish momentum, and exports ranked results to CSV.

---

## Features

✔ Download latest OHLCV data

✔ Scan all Nifty 50 stocks

✔ Calculate

- EMA 20
- EMA 50
- EMA Crossover
- RSI (14)
- MACD
- Volume Breakout

✔ Momentum Score

✔ Rank strongest stocks

✔ Export results to CSV

✔ Beginner friendly

---

## Example Output

| Rank | Symbol | Price | EMA20 | EMA50 | RSI | MACD | Volume Breakout | Score |
|------|---------|-------|-------|-------|------|-------|-----------------|------|
| 1 | RELIANCE | 3112 | Yes | Yes | 63 | Bullish | Yes | 96 |
| 2 | TCS | 4280 | Yes | Yes | 59 | Bullish | Yes | 91 |
| 3 | ICICIBANK | 1451 | Yes | Yes | 67 | Bullish | No | 88 |

---

## Folder Structure

```
nifty50-momentum-scanner/

│
├── data/
│
├── output/
│
├── config/
│     settings.py
│
├── scanner/
│     downloader.py
│     indicators.py
│     scoring.py
│     exporter.py
│
├── utils/
│     nifty50.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

## Installation

```
pip install -r requirements.txt
```

---

## Requirements

- pandas
- yfinance
- pandas-ta
- numpy

---

## Run

```
python main.py
```

---

## Output

After execution,

CSV file will be created

```
output/nifty50_momentum.csv
```

---

## Suggested Future Improvements

- Streamlit Dashboard

- Telegram Alerts

- Email Alerts

- Weekly Scanner

- Multi Time Frame Analysis

- Portfolio Watchlist

- Relative Strength Ranking

- Backtesting

---

## Disclaimer

Educational purposes only.

Not investment advice.
