import streamlit as st
from pathlib import Path

def safe_html(html_str):
    # Collapses all newlines and indentation so Streamlit's markdown parser
    # never interprets indented HTML tags as pre/code blocks.
    clean_html = ' '.join(html_str.split())
    st.markdown(clean_html, unsafe_allow_html=True)

def load_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            css_content = f.read()
        safe_html(f"<style>{css_content}</style>")