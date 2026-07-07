import streamlit as st


def render_filters():
    """
    Render stock filtering options.

    Returns
    -------
    dict
        Selected filter values.
    """

    st.subheader("🔍 Stock Filters")

    col1, col2 = st.columns(2)

    with col1:
        sector = st.selectbox(
            "Sector",
            [
                "All",
                "Banking",
                "IT",
                "Auto",
                "Pharma",
                "FMCG",
                "Metal",
                "Energy",
                "Realty",
                "Financial Services",
            ],
        )

        min_price = st.number_input(
            "Minimum Price",
            min_value=0.0,
            value=0.0,
        )

    with col2:
        max_price = st.number_input(
            "Maximum Price",
            min_value=0.0,
            value=100000.0,
        )

        min_volume = st.number_input(
            "Minimum Volume",
            min_value=0,
            value=0,
        )

    return {
        "sector": sector,
        "min_price": min_price,
        "max_price": max_price,
        "min_volume": min_volume,
    }
