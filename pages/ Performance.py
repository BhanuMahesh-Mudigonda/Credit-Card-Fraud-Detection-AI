import streamlit as st
import pandas as pd

st.title("📈 AI Performance Analytics")
st.caption("Machine Learning Model Performance Dashboard")

st.markdown("---")

st.subheader("🏆 Model Comparison")

performance = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy":[94.20,97.60,99.95,99.82],
    "Precision":[92.10,96.30,99.70,99.60],
    "Recall":[90.50,95.20,99.40,99.30],
    "F1 Score":[91.30,95.70,99.55,99.45]
})

st.dataframe(
    performance,
    use_container_width=True
)

st.markdown("---")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Best Model","Random Forest")

with c2:
    st.metric("Accuracy","99.95%")

with c3:
    st.metric("Recall","99.40%")

with c4:
    st.metric("F1 Score","99.55%")

st.markdown("---")

st.subheader("📊 Accuracy Comparison")

chart = performance.set_index("Model")["Accuracy"]

st.bar_chart(chart)

st.markdown("---")

st.subheader("🎯 AI Insights")

st.success("""
✔ Random Forest achieved the highest accuracy.

✔ Very low False Positive Rate.

✔ Excellent fraud detection capability.

✔ Suitable for real-time deployment.
""")

st.info("""
Future Enhancements

• Deep Learning Models

• Explainable AI

• Live Fraud Monitoring

• Cloud Deployment
""")