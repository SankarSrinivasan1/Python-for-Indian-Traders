import streamlit as st
import pandas as pd


def display_results(results: pd.DataFrame):
    """
    Display screener results.
    """

    st.subheader("📋 Screening Results")

    if results.empty:
        st.warning("No stocks matched the selected strategy.")
        return

    st.success(f"{len(results)} stocks found.")

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True,
    )

    csv = results.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="screening_results.csv",
        mime="text/csv",
    )


def show_summary(results: pd.DataFrame):
    """
    Display summary statistics.
    """

    if results.empty:
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Stocks",
            len(results),
        )

    with col2:
        if "Close" in results.columns:
            st.metric(
                "Average Price",
                round(results["Close"].mean(), 2),
            )

    with col3:
        if "Volume" in results.columns:
            st.metric(
                "Average Volume",
                int(results["Volume"].mean()),
            )
