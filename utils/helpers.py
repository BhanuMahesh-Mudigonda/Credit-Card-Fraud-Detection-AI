import streamlit as st

def section(title):

    st.markdown(f"## {title}")

def line():

    st.divider()

def success(text):

    st.success(text)

def warning(text):

    st.warning(text)