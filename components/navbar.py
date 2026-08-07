import streamlit as st
from datetime import datetime
from utils.theme import safe_html

NAV_ITEMS = [
    ("Home", "🏠"),
    ("Dataset", "📊"),
    ("Prediction", "🤖"),
    ("Performance", "📈"),
    ("Explain AI", "🧠"),
    ("Dashboard", "📡"),
    ("Reports", "📄"),
    ("About", "ℹ️"),
]

def render_top_navbar():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    curr = st.session_state.current_page
    now_str = datetime.now().strftime("%H:%M:%S UTC")

    navbar_html = f"""
    <div class="aegis-navbar">
        <div class="aegis-brand">
            <div class="aegis-brand-logo">🛡️</div>
            <div class="aegis-brand-text">AEGIS AI</div>
        </div>
        <div class="aegis-status-badge">
            <div class="aegis-pulse-dot"></div>
            AI ONLINE | {now_str}
        </div>
    </div>
    """
    safe_html(navbar_html)

    cols = st.columns(len(NAV_ITEMS))
    for idx, (item, icon) in enumerate(NAV_ITEMS):
        with cols[idx]:
            btn_label = f"{icon} {item}"
            if st.button(btn_label, key=f"nav_btn_{item}", use_container_width=True):
                st.session_state.current_page = item
                st.rerun()