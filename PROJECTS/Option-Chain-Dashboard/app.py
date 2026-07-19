import streamlit as st

st.set_page_config(
    page_title="Option Chain Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Option Chain Dashboard")
st.subheader("Python for Indian Stock Traders")

st.info(
    "This is the starter application.\n\n"
    "Future versions will include:\n"
    "- Live NSE Option Chain\n"
    "- PCR\n"
    "- Max Pain\n"
    "- OI Analysis\n"
    "- IV Analysis\n"
    "- ATM / ITM / OTM Detection"
)

col1, col2, col3 = st.columns(3)

col1.metric("PCR", "--")
col2.metric("Max Pain", "--")
col3.metric("ATM Strike", "--")

st.divider()

st.header("Option Chain")

st.write("No data loaded.")

st.divider()

st.caption("© Sankar Srinivasan")
