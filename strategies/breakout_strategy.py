def breakout_signal(high, resistance):
    if high > resistance:
        return "BUY"

    return "WAIT"
