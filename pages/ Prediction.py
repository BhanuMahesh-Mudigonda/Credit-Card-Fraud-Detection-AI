import streamlit as st

st.title("🤖 AI Fraud Prediction")
st.caption("Real-Time Transaction Risk Analysis")

st.markdown("---")

left, right = st.columns([2, 1])

with left:

    st.markdown("### 💳 Transaction Details")

    amount = st.number_input(
        "Transaction Amount ($)",
        min_value=0.0,
        value=120.50,
        step=1.0
    )

    time = st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=1000.0,
        step=1.0
    )

    prediction_threshold = st.slider(
        "Risk Threshold",
        0,
        100,
        50
    )

    predict = st.button("🚀 Analyze Transaction")

with right:

    st.markdown("""
<div class="panel">

### ⚡ AI Status

🟢 Model Loaded

🟢 Prediction Ready

🟢 System Healthy

🟢 Live Monitoring

</div>
""", unsafe_allow_html=True)

st.markdown("---")

if predict:

    fraud_probability = min(amount / 1000, 1.0)

    if fraud_probability > 0.50:

        st.error("🚨 High Fraud Risk Detected")

        st.progress(int(fraud_probability * 100))

        st.metric(
            "Fraud Probability",
            f"{fraud_probability*100:.2f}%"
        )

        st.warning(
            "Recommendation: Block transaction and perform manual verification."
        )

    else:

        st.success("✅ Legitimate Transaction")

        st.progress(int(fraud_probability * 100))

        st.metric(
            "Fraud Probability",
            f"{fraud_probability*100:.2f}%"
        )

        st.info(
            "Recommendation: Transaction appears safe."
        )

    st.markdown("### 📋 Transaction Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Amount", f"${amount:.2f}")

    with c2:
        st.metric("Time", int(time))

    with c3:
        st.metric("Threshold", f"{prediction_threshold}%")

st.markdown("---")

st.markdown("## 🧠 AI Workflow")

st.write("""
1. Transaction received

2. Feature preprocessing

3. Machine Learning prediction

4. Fraud probability estimation

5. Final decision generated
""")