import plotly.graph_objects as go
import streamlit as st


def price_chart(df, symbol):
    """
    Display price chart.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name=symbol,
        )
    )

    fig.update_layout(
        title=f"{symbol} Price Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        height=600,
        xaxis_rangeslider_visible=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def indicator_chart(df, column, title):
    """
    Plot a technical indicator.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[column],
            mode="lines",
            name=column,
        )
    )

    fig.update_layout(
        title=title,
        height=400,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def volume_chart(df):
    """
    Display volume bars.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Volume"],
            name="Volume",
        )
    )

    fig.update_layout(
        title="Volume",
        height=300,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def bollinger_chart(df):
    """
    Display Bollinger Bands.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            name="Close",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["BBU_20_2.0"],
            name="Upper Band",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["BBL_20_2.0"],
            name="Lower Band",
        )
    )

    fig.update_layout(
        title="Bollinger Bands",
        height=500,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def ema_chart(df):
    """
    Display EMA crossover chart.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            name="Close",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["EMA50"],
            name="EMA 50",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["EMA200"],
            name="EMA 200",
        )
    )

    fig.update_layout(
        title="EMA Crossover",
        height=500,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def rsi_chart(df):
    """
    Display RSI indicator.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["RSI"],
            name="RSI",
        )
    )

    fig.add_hline(y=70)

    fig.add_hline(y=30)

    fig.update_layout(
        title="Relative Strength Index (RSI)",
        height=350,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
