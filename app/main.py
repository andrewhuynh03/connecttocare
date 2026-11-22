"""ConnectToCare Streamlit entry point.

The first version is intentionally small. Claude Code will expand this after
the data source and data dictionary are confirmed.
"""

import streamlit as st


st.set_page_config(page_title="ConnectToCare", page_icon="🏥", layout="wide")

st.title("ConnectToCare")
st.subheader("Healthcare Appointment Intelligence")
st.info(
    "Project setup is complete. Add a public or synthetic appointment dataset, "
    "then ask Claude Code to implement the data-ingestion milestone."
)

st.markdown(
    "**Safety note:** This educational prototype is not a clinical tool and "
    "must not be used to make decisions about real patients."
)
