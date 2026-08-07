import streamlit as st
import pandas as pd

st.title("📊 Data Intelligence Center")
st.caption("Enterprise Dataset Analytics Dashboard")

st.markdown("---")

# ===========================
# Load Dataset
# ===========================

try:
    df = pd.read_csv("credit_card_fraud.csv")
except:
    st.error("Dataset not found.")
    st.stop()

# ===========================
# KPI Cards
# ===========================

rows = len(df)
cols = len(df.columns)

fraud = 492
normal = rows - fraud

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Transactions", f"{rows:,}")

with c2:
    st.metric("Fraud Cases", fraud)

with c3:
    st.metric("Legitimate", f"{normal:,}")

with c4:
    st.metric("Features", cols)

st.markdown("---")

# ===========================
# Preview
# ===========================

st.subheader("Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)

st.markdown("---")

# ===========================
# Dataset Information
# ===========================

left,right=st.columns(2)

with left:

    st.subheader("Shape")

    st.write(df.shape)

    st.subheader("Missing Values")

    st.write(df.isnull().sum())

with right:

    st.subheader("Data Types")

    st.write(df.dtypes)

st.markdown("---")

# ===========================
# Statistics
# ===========================

st.subheader("Statistical Summary")

st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

# ===========================
# Class Distribution
# ===========================

st.subheader("Fraud Distribution")

chart = pd.DataFrame({
    "Type":["Legitimate","Fraud"],
    "Count":[normal,fraud]
})

st.bar_chart(chart.set_index("Type"))

st.success("Dataset loaded successfully.")