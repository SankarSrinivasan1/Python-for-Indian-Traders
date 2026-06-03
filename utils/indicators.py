import pandas as pd

def moving_average(series, period):
    return series.rolling(period).mean()
