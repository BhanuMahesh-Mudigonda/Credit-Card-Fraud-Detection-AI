import streamlit as st
from utils.theme import safe_html, reset_scroll_to_top

PAGE_SEQUENCE = ["Home", "Dataset", "Prediction", "Performance", "Explain AI", "Dashboard", "Reports", "About"]

def footer():
    curr_page = st.session_state.get("current_page", "Home")
    curr_idx = PAGE_SEQUENCE.index(curr_page) if curr_page in PAGE_SEQUENCE else 0

    has_prev = (curr_idx > 0)
    has_next = (curr_idx < len(PAGE_SEQUENCE) - 1)

    prev_page = PAGE_SEQUENCE[curr_idx - 1] if has_prev else None
    next_page = PAGE_SEQUENCE[curr_idx + 1] if has_next else PAGE_SEQUENCE[0]

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 3-column Guided Sequential Page Controller
    c_prev, c_center, c_next = st.columns([1.2, 1.6, 1.2])
    
    with c_prev:
        if has_prev and prev_page:
            if st.button(f"← PREV: {prev_page}", key="footer_prev_btn", type="secondary", use_container_width=True):
                st.session_state.current_page = prev_page
                reset_scroll_to_top()
                st.rerun()

    with c_center:
        center_html = f"""
        <div style="text-align: center; background: rgba(10, 15, 36, 0.7); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 12px; padding: 7px 14px;">
            <div style="font-size: 0.72rem; color: #00F0FF; font-weight: 800; letter-spacing: 1.5px; text-transform: uppercase;">
                MODULE {curr_idx + 1} OF 8 • {curr_page.upper()}
            </div>
            <div style="font-size: 0.68rem; color: #94A3B8;">AEGIS FRAUD INTELLIGENCE FLOW</div>
        </div>
        """
        safe_html(center_html)

    with c_next:
        next_label = f"NEXT: {next_page} →" if has_next else f"🔄 START OVER: {next_page}"
        if st.button(next_label, key="footer_next_btn", type="primary", use_container_width=True):
            st.session_state.current_page = next_page
            reset_scroll_to_top()
            st.rerun()

    st.markdown(
        """
        <div style="text-align: center; margin-top: 1.8rem; padding-bottom: 2rem; color: #94A3B8; font-size: 0.82rem; letter-spacing: 0.5px;">
            🛡️ AEGIS AI Enterprise Fraud Intelligence & Financial Security Operations Center | © 2026 AEGIS AI
        </div>
        """,
        unsafe_allow_html=True
    )