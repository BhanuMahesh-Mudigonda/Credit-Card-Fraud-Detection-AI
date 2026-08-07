import streamlit as st
from datetime import datetime

st.title("📄 AI Fraud Report")
st.caption("Generate Transaction Report")

st.markdown("---")

st.subheader("Latest Prediction")

st.success("Transaction : Legitimate")

st.metric("Confidence","99.82%")

st.metric("Risk","Low")

st.metric("Recommendation","Proceed")

st.markdown("---")

st.write("Generated On")

st.code(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.download_button(
    "⬇ Download Report",
    data="""
AI Fraud Detection Report

Status : Legitimate

Confidence : 99.82%

Recommendation : Proceed
""",
    file_name="fraud_report.txt"
)

st.success("Report Ready.")