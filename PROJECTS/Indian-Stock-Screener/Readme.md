# 🇮🇳 Indian Stock Screener

A fast and interactive stock screener built with **Python**, **Streamlit**, and **pandas-ta** for Indian stock traders.

Screen hundreds of NSE-listed stocks in seconds using popular technical indicators and instantly discover trading opportunities.

---

## ✨ Features

- 📊 Scan Indian stocks with one click
- ⚡ Fast technical analysis using pandas-ta
- 🎯 Interactive Streamlit dashboard
- 📈 Multiple screening strategies
- 📋 Download screening results
- 🔍 Beginner-friendly interface

---

## Supported Screening Strategies

Choose one or more strategies.

### RSI Oversold
Find stocks where

```
RSI < 30
```

Ideal for potential reversal opportunities.

---

### RSI Overbought

Find stocks where

```
RSI > 70
```

Useful for identifying overextended moves.

---

### Golden Cross

Detect stocks where

```
50 EMA crosses above 200 EMA
```

A popular long-term bullish signal.

---

### Supertrend Buy

Find stocks currently trading above the Supertrend indicator.

Useful for trend-following traders.

---

### ADX Strong Trend

Filter stocks where

```
ADX > User Defined Value
```

Identifies stocks in strong trends.

---

### Bollinger Band Breakout

Find stocks breaking above the upper Bollinger Band.

Useful for momentum and breakout trading.

---

## Dashboard

The application allows users to

- Select screening strategy
- Choose indicator parameters
- Scan all supported stocks
- View matching stocks
- Sort results
- Export results to CSV

---

## Technology Stack

- Python 3.11+
- Streamlit
- pandas
- pandas-ta
- yfinance (or your preferred market data source)
- NumPy

---

## Installation

Clone the repository.

```bash
git clone 
https://github.com/SankarSrinivasan1/Python-for-Indian-Traders/tree/main/PROJECTS/Indian-Stock-Screener.git
```

Move into the project.

```bash
cd indian-stock-screener
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Start the application.

```bash
streamlit run app.py
```

---

## Project Structure

```
Indian-Stock-Screener/
│
├── app.py
├── requirements.txt
├── config.py
├── data/
├── indicators/
├── screener/
├── utils/
├── assets/
├── README.md
└── LICENSE
```

---

## Example Workflow

1. Launch the Streamlit app
2. Select a screening strategy
3. Configure indicator values
4. Click **Run Screener**
5. View qualifying stocks
6. Export results if needed

---

## Future Enhancements

- Multiple timeframe analysis
- Candlestick pattern detection
- MACD Scanner
- EMA Crossover Scanner
- VWAP Scanner
- Pivot Point Scanner
- Volume Breakout Scanner
- Relative Strength Scanner
- Telegram Alerts
- Email Notifications
- Portfolio Tracking
- Watchlist Management

---

## Disclaimer

This project is for educational and research purposes only.

It is **not financial advice**. Always perform your own analysis before making investment decisions.

---

## Contributing

Pull requests are welcome.

If you have ideas for additional screening strategies, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful,

⭐ Star the repository

🍴 Fork it

💡 Share it with fellow traders

Happy Coding and Happy Trading!

© Sankar Srinivasan 
petra.srini@gmail.com

---

# GitHub companion repository for book titled:
![Python for Indian Stock Traders](https://github.com/SankarSrinivasan1/Python-for-Indian-Traders/blob/main/utils/python%201j.jpg)

## Buy the book at Amazon and leading online bookstores
[Python for Indian Stock Traders](https://www.amazon.in/Python-Indian-Stock-Traders-Analytics-ebook/dp/B0H3ZL3JF1)
