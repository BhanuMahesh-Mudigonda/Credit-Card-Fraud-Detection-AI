import streamlit as st
import plotly.graph_objects as go
from utils.theme import safe_html
from components.charts import CYBER_LAYOUT

def render_explain_ai_view():
    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">🧠 EXPLAINABLE AI (XAI) & SHAP FEATURE ATTRIBUTION</div>
                <div class="panel-subtitle">Transparent AI decision explanations for banking compliance and SOC auditors</div>
            </div>
            <span class="badge-approved">SHAP ENGINE ACTIVE</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("### 📊 Top Feature Importance Ranking (XGBoost SHAP Values)")
        features = ['V14 (Identity Anomaly)', 'V10 (Device Fingerprint)', 'V12 (Geo Velocity)', 'V4 (Txn Frequency)', 'Transaction Amount ($)', 'V17 (Pattern Spike)', 'V11 (User Agent)', 'V7 (Account Age)']
        importance = [0.28, 0.22, 0.18, 0.12, 0.09, 0.05, 0.04, 0.02]

        fig = go.Figure(go.Bar(
            x=importance, y=features, orientation='h',
            marker=dict(color=importance, colorscale=[[0, '#00D4FF'], [1, '#7C3AED']])
        ))
        fig.update_layout(CYBER_LAYOUT)
        fig.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### 🔍 Single Transaction SHAP Waterfall Plot")
        fig_waterfall = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "relative", "total"],
            x=["Base Rate", "V14 (-5.2)", "Amount ($4.5k)", "V10 (-3.1)", "V12 (-2.4)", "Final Score"],
            textposition="outside",
            text=["0.02", "+0.45", "+0.25", "+0.15", "+0.08", "0.95"],
            y=[0.02, 0.45, 0.25, 0.15, 0.08, 0],
            connector={"line": {"color": "rgba(0, 212, 255, 0.5)"}},
            decreasing={"marker": {"color": "#22C55E"}},
            increasing={"marker": {"color": "#EF4444"}},
            totals={"marker": {"color": "#00D4FF"}}
        ))
        fig_waterfall.update_layout(CYBER_LAYOUT)
        fig_waterfall.update_layout(title=dict(text="Transaction #89421 SHAP Attribution", font=dict(color="#FFFFFF", size=13)))
        st.plotly_chart(fig_waterfall, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📋 Automated Compliance & Threat Explanation Audit")
    expl_html = """
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
        <div class="feed-item" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="color: #00D4FF; font-weight: 700;">1. IDENTITY ANOMALY (V14)</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">V14 deviation of -5.2 indicates synthetic identity signature or hijacked authorization tokens.</div>
        </div>
        <div class="feed-item" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="color: #7C3AED; font-weight: 700;">2. GEO VELOCITY SPIKE (V12)</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">Impossibility check triggered: 2 transactions in NYC and Tokyo within 8 minutes.</div>
        </div>
        <div class="feed-item" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="color: #EF4444; font-weight: 700;">3. AMOUNT DEVIATION</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">Transaction amount is 52x higher than historical 90-day account baseline.</div>
        </div>
    </div>
    """
    safe_html(expl_html)
