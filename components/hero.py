import streamlit as st
import matplotlib.pyplot as plt

def accuracy_chart():

    models = [
        "Logistic",
        "Decision Tree",
        "Random Forest",
        "XGBoost"
    ]

    acc = [
        97.8,
        99.1,
        99.95,
        99.92
    ]

    fig,ax=plt.subplots(figsize=(8,4))

    ax.bar(models,acc)

    ax.set_ylabel("Accuracy")

    st.pyplot(fig)