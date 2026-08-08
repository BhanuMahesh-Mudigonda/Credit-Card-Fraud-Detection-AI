import streamlit as st
from utils.theme import safe_html

def render_world_network():
    """Renders the Fraud Feature Threat Landscape PCA scatter plot based on actual dataset features V14 vs V10."""
    from utils.dataset_loader import get_sample_dataset
    import plotly.express as px
    from components.charts import CYBER_LAYOUT

    df = get_sample_dataset(800)
    fig = px.scatter(
        df, x='V14', y='V10', color='Class',
        color_discrete_map={0: '#00F0FF', 1: '#EF4444'},
        labels={'Class': 'Transaction Class', 'V14': 'V14 (Identity Integrity)', 'V10': 'V10 (Device Fingerprint)'},
        hover_data=['Amount', 'Time'],
        title="🌐 FRAUD FEATURE THREAT LANDSCAPE (V14 vs V10 Discriminant Cluster)"
    )
    layout = CYBER_LAYOUT.copy()
    layout.update(
        height=380,
        legend=dict(orientation='h', y=-0.18, x=0.2),
        margin=dict(l=40, r=40, t=60, b=50)
    )
    fig.update_layout(layout)
    st.plotly_chart(fig, use_container_width=True)

def render_live_feed():
    """Renders honest data-driven AEGIS Inference Command Stream from st.session_state.prediction_history."""
    history = st.session_state.get("prediction_history", [])
    
    if not history:
        feed_items_html = """
        <div style="text-align: center; padding: 2rem 1rem; color: #94A3B8;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 12px;">
                <span style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10B981; color: #10B981; padding: 4px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 800;">● MODEL READY</span>
                <span style="background: rgba(0, 240, 255, 0.15); border: 1px solid #00F0FF; color: #00F0FF; padding: 4px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 800;">● PIPELINE ONLINE</span>
                <span style="background: rgba(139, 92, 246, 0.15); border: 1px solid #8B5CF6; color: #8B5CF6; padding: 4px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 800;">● XGBOOST ACTIVE</span>
            </div>
            
            <svg viewBox="0 0 200 200" style="width: 140px; height: 140px; margin: 10px auto;">
                <circle cx="100" cy="100" r="80" fill="none" stroke="rgba(0, 240, 255, 0.15)" stroke-width="3"/>
                <circle cx="100" cy="100" r="60" fill="none" stroke="rgba(0, 240, 255, 0.3)" stroke-width="2" stroke-dasharray="8 6"/>
                <circle cx="100" cy="100" r="40" fill="rgba(0, 240, 255, 0.08)" stroke="#00F0FF" stroke-width="2">
                    <animate attributeName="r" values="35;45;35" dur="3s" repeatCount="indefinite"/>
                </circle>
                <circle cx="100" cy="100" r="10" fill="#00F0FF"/>
                <line x1="100" y1="100" x2="160" y2="100" stroke="#00F0FF" stroke-width="2">
                    <animateTransform attributeName="transform" type="rotate" from="0 100 100" to="360 100 100" dur="4s" repeatCount="indefinite"/>
                </line>
            </svg>
            
            <div style="font-weight: 700; color: #FFFFFF; font-size: 1rem; margin-top: 6px;">NO PREDICTION EVENTS IN CURRENT SESSION</div>
            <div style="font-size: 0.82rem; color: #64748B; margin-top: 4px; max-width: 320px; margin-left: auto; margin-right: auto;">
                Generate a real prediction from the Prediction Studio to populate this command stream.
            </div>
        </div>
        """
    else:
        feed_items_html = ""
        for item in reversed(history[-6:]):
            badge_cls = "badge-blocked" if item['risk'] >= 50.0 else "badge-approved"
            feed_items_html += f"""
            <div class="feed-item" style="border-left: 3px solid {'#EF4444' if item['risk'] >= 50.0 else '#10B981'}; margin-bottom: 8px;">
                <div class="feed-country">
                    <span style="font-size: 1.3rem;">{'🚨' if item['risk'] >= 50.0 else '✅'}</span>
                    <div>
                        <div style="font-weight: 800; color: #FFFFFF;">Session Txn #{item['id']}</div>
                        <div style="font-size: 0.75rem; color: #94A3B8;">{item['channel']} • {item['timestamp']}</div>
                    </div>
                </div>
                <div style="text-align: right;">
                    <div class="feed-amount" style="font-weight: 800;">${item['amount']:,.2f}</div>
                    <span class="{badge_cls}" style="font-size: 0.72rem;">{item['decision']} ({item['risk']:.1f}% Risk)</span>
                </div>
            </div>
            """

    feed_html = f"""
    <div class="aegis-panel" style="height: 100%; min-height: 440px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
            <div class="panel-header">
                <div>
                    <div class="panel-title">📡 AEGIS INFERENCE COMMAND STREAM</div>
                    <div class="panel-subtitle">Real-time XGBoost inference event telemetry</div>
                </div>
                <span class="badge-approved">{len(history)} SESSION EVENTS</span>
            </div>
            <div class="live-feed-container">
                {feed_items_html}
            </div>
        </div>
    </div>
    """
    safe_html(feed_html)
    
    if st.button("🚀 EXECUTE TEST PREDICTION SCAN", key="cmd_stream_run_btn", use_container_width=True):
        st.session_state.current_page = "Prediction"
        st.rerun()
