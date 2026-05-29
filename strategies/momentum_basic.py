def momentum_signal(current_price, previous_price):
    if current_price > previous_price:
        return "UPTREND"

    return "DOWNTREND"
