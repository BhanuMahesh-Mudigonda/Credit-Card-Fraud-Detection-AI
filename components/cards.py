import streamlit as st

def glass_card(title, value, subtitle=""):
    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,0.08);
        padding:25px;
        border-radius:20px;
        border:1px solid rgba(255,255,255,0.15);
        backdrop-filter:blur(12px);
        margin-bottom:15px;
        box-shadow:0 8px 25px rgba(0,0,0,0.25);
    ">
        <h4>{title}</h4>
        <h2>{value}</h2>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)