import streamlit as st


def render_sidebar():
    """
    Render the application's sidebar.

    Returns
    -------
    dict
        Dictionary containing user-selected options.
    """

    st.sidebar.title("🇮🇳 Indian Stock Screener")

    st.sidebar.markdown("---")

    strategy = st.sidebar.selectbox(
        "Select Screening Strategy",
        (
            "RSI Oversold (<30)",
            "RSI Overbought (>70)",
            "Golden Cross",
            "Supertrend Buy",
            "ADX Trend",
            "Bollinger Breakout",
        ),
    )

    st.sidebar.markdown("### Indicator Settings")

    rsi_period = st.sidebar.slider(
        "RSI Period",
        min_value=5,
        max_value=30,
        value=14,
    )

    ema_fast = st.sidebar.number_input(
        "Fast EMA",
        min_value=5,
        max_value=100,
        value=50,
    )

    ema_slow = st.sidebar.number_input(
        "Slow EMA",
        min_value=50,
        max_value=300,
        value=200,
    )

    adx_period = st.sidebar.slider(
        "ADX Period",
        min_value=5,
        max_value=30,
        value=14,
    )

    adx_threshold = st.sidebar.slider(
        "Minimum ADX",
        min_value=10,
        max_value=50,
        value=25,
    )

    st.sidebar.markdown("---")

    scan_button = st.sidebar.button(
        "🚀 Run Screener",
        use_container_width=True,
    )

    return {
        "strategy": strategy,
        "rsi_period": rsi_period,
        "ema_fast": ema_fast,
        "ema_slow": ema_slow,
        "adx_period": adx_period,
        "adx_threshold": adx_threshold,
        "scan": scan_button,
    }
