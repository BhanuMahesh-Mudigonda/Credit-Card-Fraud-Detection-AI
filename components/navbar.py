import streamlit as st
from datetime import datetime
from utils.theme import safe_html, reset_scroll_to_top

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
    from utils.dataset_loader import get_dataset_summary
    from utils.model_loader import get_model_validation_metrics
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    curr = st.session_state.current_page
    now_str = datetime.now().strftime("%H:%M:%S UTC")
    
    d_stats = get_dataset_summary()
    m_stats = get_model_validation_metrics()

    navbar_html = f"""
    <div class="aegis-navbar">
        <div class="aegis-brand">
            <div class="aegis-brand-logo">🛡️</div>
            <div>
                <div class="aegis-brand-text">AEGIS AI</div>
                <div style="font-size: 0.65rem; color: #FFD700; letter-spacing: 1.5px; font-weight: 700; text-transform: uppercase; line-height: 1;">ACADEMIC & SOC COMMAND</div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 15px; flex-wrap: wrap;">
            <div style="display: flex; align-items: center; gap: 6px; background: rgba(0, 240, 255, 0.1); border: 1px solid rgba(0, 240, 255, 0.3); padding: 5px 14px; border-radius: 20px; font-size: 0.78rem; color: #00F0FF; font-weight: 700;">
                📊 {d_stats['total_rows']:,} SAMPLES | XGBOOST (AUC {m_stats['test_auc']:.4f})
            </div>
            <div class="aegis-status-badge">
                <div class="aegis-pulse-dot"></div>
                AI ONLINE | {now_str}
            </div>
        </div>
    </div>
    """
    safe_html(navbar_html)

    cols = st.columns(len(NAV_ITEMS))
    for idx, (item, icon) in enumerate(NAV_ITEMS):
        with cols[idx]:
            is_active = (item == curr)
            btn_label = f"{icon} {item}"
            btn_type = "primary" if is_active else "secondary"
            if st.button(btn_label, key=f"nav_btn_{item}", type=btn_type, use_container_width=True):
                st.query_params["page"] = item
                st.rerun()