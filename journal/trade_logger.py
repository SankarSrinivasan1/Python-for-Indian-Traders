import csv

def log_trade(symbol, entry, exit_price):
    with open("trades.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([symbol, entry, exit_price])
