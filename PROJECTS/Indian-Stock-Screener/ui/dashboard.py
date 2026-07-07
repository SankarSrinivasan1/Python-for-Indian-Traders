import streamlit as st


def render_dashboard():
    """
    Display the application dashboard.
    """

    st.set_page_config(
        page_title="Indian Stock Screener",
        page_icon="📈",
        layout="wide",
    )

    st.title("🇮🇳 Indian Stock Screener")

    st.caption(
        "Screen NSE stocks instantly using popular technical indicators."
    )

    st.markdown("---")


def display_statistics(total_scanned, qualified):
    """
    Display dashboard statistics.
    """

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Stocks Scanned",
            value=total_scanned,
        )

    with col2:
        st.metric(
            label="Qualified Stocks",
            value=qualified,
        )

    with col3:
        percentage = (
            round((qualified / total_scanned) * 100, 2)
            if total_scanned > 0
            else 0
        )

        st.metric(
            label="Success Rate",
            value=f"{percentage}%",
        )


def show_status(message):
    """
    Display information message.
    """

    st.info(message)


def show_success(message):
    """
    Display success message.
    """

    st.success(message)


def show_error(message):
    """
    Display error message.
    """

    st.error(message)


def show_warning(message):
    """
    Display warning message.
    """

    st.warning(message)
