import streamlit as st
from utils.theme import load_css

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AEGIS AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load Premium CSS
# -----------------------------
load_css()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("# 🛡️ AEGIS AI")

    st.caption("Enterprise Fraud Intelligence Platform")

    st.divider()

    st.success("🟢 AI ONLINE")

    st.metric("Accuracy","99.95%")

    st.metric("Fraud Cases","492")

    st.metric("Transactions","284,807")

    st.divider()

    st.info("""
Use the pages below to navigate.

🏠 Home

📊 Dataset

🤖 Prediction

📈 Performance

🧠 Explain AI

📡 Live Dashboard

📄 Reports

ℹ️ About
""")

# -----------------------------
# Main Dashboard
# -----------------------------

st.title("🛡️ AEGIS AI")

st.subheader("Enterprise Fraud Intelligence Platform")

st.write("")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Transactions","284,807","+18%")

with c2:
    st.metric("Fraud Alerts","492","-2%")

with c3:
    st.metric("Accuracy","99.95%","+0.3%")

with c4:
    st.metric("AI Status","ONLINE","🟢")

st.divider()

st.markdown("""
### 🚀 Welcome

AEGIS AI is an enterprise-grade credit card fraud detection platform built
using Machine Learning and Streamlit.

Navigate through the sidebar to explore:

- 📊 Dataset Analytics
- 🤖 AI Prediction
- 📈 Performance Dashboard
- 🧠 Explain AI
- 📡 Live Monitoring
- 📄 Reports
- ℹ️ About
""")

st.success("✔ Premium Theme Loaded Successfully")