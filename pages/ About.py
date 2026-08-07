import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About This Project")
st.markdown("### Credit Card Fraud Detection using Machine Learning")

st.divider()

st.markdown("""
<div style="
background:linear-gradient(90deg,#1e3c72,#2a5298);
padding:25px;
border-radius:15px;
color:white;
">

<h2>💳 Credit Card Fraud Detection System</h2>

<p style="font-size:18px;">
This web application is designed to detect fraudulent credit card transactions
using Machine Learning algorithms. The system analyzes transaction details and
predicts whether the transaction is Legitimate or Fraudulent in real time.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### 🚀 Technologies Used

✅ Python

✅ Streamlit

✅ Pandas

✅ NumPy

✅ Scikit-Learn

✅ Matplotlib

✅ Joblib
""")

with col2:
    st.markdown("""
### 🤖 Machine Learning Models

✔ Logistic Regression

✔ Decision Tree

✔ Random Forest

✔ XGBoost
""")

st.divider()

st.markdown("""
### 🎯 Key Features

- 🔍 Real-Time Fraud Detection

- 📊 Dataset Analysis

- 📈 Model Performance Comparison

- 🤖 Machine Learning Prediction

- 🌐 Interactive Web Dashboard

- ⚡ Fast and User Friendly Interface
""")

st.divider()

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Dataset", "284,807")

with col4:
    st.metric("Fraud Cases", "492")

with col5:
    st.metric("Best Accuracy", "99.95%")

st.divider()

st.success("🏆 Random Forest achieved the highest accuracy among all models.")

st.info("""
Future Improvements

• Live Banking API Integration

• Deep Learning Models

• Real-Time Transaction Monitoring

• Cloud Deployment

• AI Powered Fraud Analytics
""")

st.divider()

st.markdown(
"""
<center>

<h3>Developed for Capstone Project</h3>

Credit Card Fraud Detection using Machine Learning

Made with ❤️ using Streamlit

</center>
""",
unsafe_allow_html=True
)