import pandas as pd
import requests


def fetch_sample_data():
    data = {
        "symbol": ["RELIANCE", "TCS", "INFY"],
        "price": [2850, 3900, 1480]
    }

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    print(fetch_sample_data())
