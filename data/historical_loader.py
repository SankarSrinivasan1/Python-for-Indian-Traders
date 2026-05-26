import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_csv("sample_data.csv")
    print(df.head())
