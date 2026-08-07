import streamlit as st
import random

st.title("🌍 Live Monitoring Dashboard")
st.caption("Enterprise Fraud Monitoring")

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Transactions", random.randint(284000,285000))

with c2:
    st.metric("Threat Level","LOW")

with c3:
    st.metric("AI Status","ONLINE")

with c4:
    st.metric("Server","Healthy")

st.markdown("---")

st.subheader("System Health")

st.progress(98)

st.success("AI Prediction Engine Running Successfully")

st.markdown("---")

st.subheader("Live Fraud Activity")

chart = {
    "Fraud":[2,4,3,5,2,1,4],
    "Safe":[98,96,97,95,98,99,96]
}

st.line_chart(chart)

st.info("Real-time monitoring simulation.")