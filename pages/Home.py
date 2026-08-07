import streamlit as st

st.title("🛡️ AI FRAUD COMMAND CENTER")
st.caption("Enterprise Fraud Intelligence Platform")

st.markdown("---")

st.markdown(
"""
<div class="hero">

<div class="live">SYSTEM ONLINE</div>

<br>

<h1 class="hero-title">
Protect Every Transaction
</h1>

<p class="hero-sub">
AI-powered real-time fraud detection platform built using Machine Learning.
Monitor transactions, detect suspicious activity and visualize insights
through an enterprise dashboard.
</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Transactions", "284,807", "+18%")

with col2:
    st.metric("Fraud Cases", "492", "-2%")

with col3:
    st.metric("Accuracy", "99.95%", "+0.3%")

with col4:
    st.metric("Status", "LIVE", "🟢")

st.write("")
st.markdown("## 📊 AI Monitoring Dashboard")

left, right = st.columns([2,1])

with left:

    st.markdown(
    """
    <div class="panel">

    <h3>🧠 AI Security Overview</h3>

    <p>
    The AI engine continuously analyzes transaction behaviour,
    identifies suspicious activities and estimates fraud probability
    using trained machine learning models.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.progress(98)

    st.success("AI Model Health : Excellent")

with right:

    st.markdown(
    """
    <div class="panel">

    <h3>⚡ Live System</h3>

    ✅ Prediction Engine

    <br><br>

    ✅ Dataset Connected

    <br><br>

    ✅ Model Loaded

    <br><br>

    ✅ Ready for Detection

    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")

st.markdown("## 📈 Platform Highlights")

a,b,c = st.columns(3)

with a:

    st.markdown(
    """
    <div class="ai-card">

    <h3>🤖 Machine Learning</h3>

    Logistic Regression

    Decision Tree

    Random Forest

    XGBoost

    </div>
    """,
    unsafe_allow_html=True
    )

with b:

    st.markdown(
    """
    <div class="ai-card">

    <h3>💳 Dataset</h3>

    284,807 Transactions

    492 Fraud Cases

    30 Features

    Highly Imbalanced Dataset

    </div>
    """,
    unsafe_allow_html=True
    )

with c:

    st.markdown(
    """
    <div class="ai-card">

    <h3>🚀 Performance</h3>

    Accuracy : 99.95%

    Precision : High

    Recall : Excellent

    F1 Score : Strong

    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")
st.divider()

st.info("💡 Navigate through Dataset, Prediction, Performance and About pages from the sidebar.")