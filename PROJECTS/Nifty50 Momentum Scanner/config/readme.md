# Future Configuration Roadmap

The `settings.py` file is intentionally designed to be scalable and easy to extend. As the project evolves, all configurable options should continue to be managed from this single location, making the application easier to customize without modifying the core source code.

## Planned Future Settings

### Telegram Notifications

Configure Telegram alerts for momentum scan results.

Example settings:

- Bot Token
- Chat ID
- Alert Enable/Disable
- Alert Frequency

---

### Email Notifications

Configure email alerts for daily or weekly scan reports.

Example settings:

- SMTP Server
- SMTP Port
- Sender Email
- Recipient Email
- App Password
- Enable/Disable Email Alerts

---

### Watchlist Scanner

Allow users to scan only selected stocks instead of the entire Nifty 50.

Example settings:

- Watchlist Symbols
- Custom Watchlist File
- Maximum Stocks
- Watchlist Name

---

### Sector-wise Scanning

Enable scanning and ranking by market sectors.

Examples:

- Banking
- Information Technology
- FMCG
- Auto
- Pharma
- Metals
- Energy
- Financial Services

---

### Relative Strength Analysis

Add configurable settings for comparing stocks against benchmark indices.

Example settings:

- Benchmark Index
- Relative Strength Period
- Ranking Method

---

### ATR and Supertrend

Support additional trend-following indicators.

Example settings:

- ATR Period
- ATR Multiplier
- Supertrend Period
- Supertrend Multiplier

---

### Multi-Timeframe Analysis

Analyze stocks across multiple timeframes before assigning a momentum score.

Supported timeframes may include:

- Daily
- Weekly
- Monthly

Future settings:

- Enable Multi-Timeframe Analysis
- Required Bullish Timeframes
- Weight per Timeframe

---

### Backtesting

Configure historical testing of momentum strategies.

Example settings:

- Start Date
- End Date
- Initial Capital
- Brokerage Charges
- Slippage
- Position Size
- Risk per Trade

---

### AI-Based Momentum Scoring

Future versions may incorporate machine learning models to enhance stock ranking.

Potential settings:

- AI Model Selection
- Prediction Confidence Threshold
- Feature Importance
- Model Version
- Enable AI Scoring

---

## Design Philosophy

Centralizing all configurable values inside `settings.py` provides several benefits:

- Single source of truth for project configuration
- Cleaner and more maintainable source code
- Easier customization for end users
- Reduced risk of hard-coded values throughout the project
- Simplified upgrades and feature additions
- Improved scalability as the project grows

As new features are introduced, corresponding configuration options should be added to `settings.py` rather than embedded directly into the application logic.
