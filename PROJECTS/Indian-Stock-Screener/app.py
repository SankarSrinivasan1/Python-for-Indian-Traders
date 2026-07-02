import streamlit as st

from config import APP_NAME, APP_VERSION
from settings import AVAILABLE_SCREENERS

st.set_page_config(
    page_title=APP_NAME,
    layout="wide"
)

st.title(APP_NAME)

st.caption(f"Version {APP_VERSION}")

st.sidebar.header("Screening Strategy")

strategy = st.sidebar.selectbox(
    "Choose Strategy",
    AVAILABLE_SCREENERS
)

st.write("### Selected Strategy")

st.success(strategy)

st.info(
    "Project setup completed.\n\n"
    "The screening engine will be connected in the next modules."
)

st.button("Run Screener")

st.divider()

st.subheader("Results")

st.write(
    "Qualifying stocks will appear here after integrating "
    "the screener engine."
)
