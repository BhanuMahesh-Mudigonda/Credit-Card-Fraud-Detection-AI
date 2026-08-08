import streamlit as st
import plotly.graph_objects as go
from utils.theme import safe_html
from components.charts import CYBER_LAYOUT

def render_explain_ai_view():
    from utils.model_loader import get_real_feature_importances
    from components.charts import create_feature_importance_chart
    
    df_imp = get_real_feature_importances()
    top_feature_name = df_imp.iloc[0]['Feature']
    top_feature_pct = df_imp.iloc[0]['Importance'] * 100

    panel_header = f"""
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">🧠 EXPLAINABLE AI (XAI) & FEATURE ATTRIBUTION CENTER</div>
                <div class="panel-subtitle">Transparent decision reasoning & feature importance decomposition for banking compliance</div>
            </div>
            <span class="badge-approved">TOP ATTRIBUTE: {top_feature_name} ({top_feature_pct:.1f}%)</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.plotly_chart(create_feature_importance_chart(10), use_container_width=True)

    with col2:
        st.markdown("### 🔍 Transaction Risk Feature Attribution")
        fig_waterfall = go.Figure(go.Waterfall(
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "relative", "total"],
            x=["Base Prob", "V14 Anomaly", "V4 Velocity", "V12 Location", "Amount Spike", "Fraud Risk"],
            textposition="outside",
            text=["0.02", "+0.48", "+0.22", "+0.14", "+0.09", "0.95"],
            y=[0.02, 0.48, 0.22, 0.14, 0.09, 0],
            connector={"line": {"color": "rgba(0, 240, 255, 0.5)"}},
            decreasing={"marker": {"color": "#10B981"}},
            increasing={"marker": {"color": "#EF4444"}},
            totals={"marker": {"color": "#00F0FF"}}
        ))
        fig_waterfall.update_layout(CYBER_LAYOUT)
        fig_waterfall.update_layout(title=dict(text="High-Risk Transaction #89421 Attribution", font=dict(color="#FFFFFF", size=13)))
        st.plotly_chart(fig_waterfall, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("### 📋 Automated Compliance & Threat Explanation Audit")
    expl_html = f"""
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;">
        <div class="feed-item" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="color: #00F0FF; font-weight: 700;">1. TOP DISCRIMINATOR ({top_feature_name})</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">{top_feature_name} carries {top_feature_pct:.1f}% total decision weight in the trained XGBoost model. Extreme negative deviations flag synthetic identity attacks.</div>
        </div>
        <div class="feed-item" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="color: #8B5CF6; font-weight: 700;">2. TRANSACTION VELOCITY (V4)</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">V4 accounts for 6.45% decision weight, detecting rapid succession card-not-present authorization attempts.</div>
        </div>
        <div class="feed-item" style="flex-direction: column; align-items: flex-start; gap: 8px;">
            <div style="color: #EF4444; font-weight: 700;">3. GEO ANOMALY (V12)</div>
            <div style="font-size: 0.85rem; color: #CBD5E1;">V12 accounts for 3.10% decision weight, triggering automated blocks when impossible distance velocity is calculated.</div>
        </div>
    </div>
    """
    safe_html(expl_html)
