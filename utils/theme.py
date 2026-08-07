import streamlit as st
from pathlib import Path

def load_css():

    css_files = [
        "styles/style.css",
        "styles/glass.css",
        "styles/animations.css"
    ]

    css = ""

    for file in css_files:

        path = Path(file)

        if path.exists():

            with open(path, encoding="utf-8") as f:

                css += f.read()

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


def page_config(title="AI Fraud Command Center"):

    st.set_page_config(
        page_title=title,
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    load_css()