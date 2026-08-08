import base64
import os
import streamlit as st

def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
            return f"data:image/png;base64,{base64.b64encode(data).decode()}"
    return ""

def section(title):
    st.markdown(f"## {title}")

def line():
    st.divider()

def success(text):
    st.success(text)

def warning(text):
    st.warning(text)