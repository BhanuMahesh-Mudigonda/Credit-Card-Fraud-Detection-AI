import streamlit as st
import pandas as pd

st.title("🧠 Explain AI")
st.caption("Why did the model predict fraud?")

st.markdown("---")

st.subheader("Feature Importance")

importance = pd.DataFrame({
    "Feature": ["Amount", "Time", "V14", "V17", "V12", "Others"],
    "Importance": [45, 18, 14, 10, 8, 5]
})

st.bar_chart(importance.set_index("Feature"))

st.markdown("---")

st.subheader("Prediction Explanation")

st.success("""
✔ High transaction amount increased fraud risk.

✔ Unusual transaction timing influenced prediction.

✔ V14 and V17 strongly contributed to the model decision.

✔ Overall confidence is very high.
""")

st.metric("AI Confidence", "99.82%")

st.info("This explanation helps users understand why the AI made its prediction.")