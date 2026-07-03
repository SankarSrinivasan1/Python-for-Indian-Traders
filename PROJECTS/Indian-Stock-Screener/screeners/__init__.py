"""
Indian Stock Screener

Screening Modules Package

Each screener exposes a single function:

screen(df) -> bool

The function returns True if the stock satisfies
the screening condition, otherwise False.
"""

from .rsi_oversold import screen as rsi_oversold
from .rsi_overbought import screen as rsi_overbought
from .golden_cross import screen as golden_cross
from .supertrend_buy import screen as supertrend_buy
from .adx_trend import screen as adx_trend
from .bollinger_breakout import screen as bollinger_breakout
