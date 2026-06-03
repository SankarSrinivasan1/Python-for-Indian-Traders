import pandas as pd

def run_backtest(df):
    profit = 0

    for i in range(1, len(df)):
        profit += df["close"].iloc[i] - df["close"].iloc[i - 1]

    return profit
