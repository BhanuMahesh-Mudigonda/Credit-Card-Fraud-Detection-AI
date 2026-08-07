import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.theme import safe_html
from utils.dataset_loader import get_sample_dataset, get_country_fraud_stats
from components.charts import create_bar_chart, CYBER_LAYOUT

def render_dataset_view():
    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">📊 GLOBAL TRANSACTION DATASET ANALYTICS</div>
                <div class="panel-subtitle">European credit card dataset snapshot with 28 PCA threat features</div>
            </div>
            <span class="badge-approved">284,807 SAMPLES LOADED</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        safe_html("""
        <div class="aegis-metric-card">
            <div class="metric-title">Total Records</div>
            <div class="metric-value">284,807</div>
            <div class="metric-delta delta-positive">Full SOC History</div>
        </div>
        """)
    with c2:
        safe_html("""
        <div class="aegis-metric-card">
            <div class="metric-title">Fraud Class Count</div>
            <div class="metric-value">492</div>
            <div class="metric-delta delta-negative">0.172% Imbalance</div>
        </div>
        """)
    with c3:
        safe_html("""
        <div class="aegis-metric-card">
            <div class="metric-title">PCA Attributes</div>
            <div class="metric-value">28</div>
            <div class="metric-delta delta-positive">V1 to V28 Encrypted</div>
        </div>
        """)
    with c4:
        safe_html("""
        <div class="aegis-metric-card">
            <div class="metric-title">Avg Transaction</div>
            <div class="metric-value">$88.35</div>
            <div class="metric-delta delta-neutral">Max $25,691</div>
        </div>
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.plotly_chart(create_bar_chart(), use_container_width=True)
    with col2:
        df = get_sample_dataset()
        fig = px.scatter(df, x='V14', y='V10', color='Class', color_discrete_map={0: '#00D4FF', 1: '#EF4444'},
                         title="🔍 PCA DISCRIMINANT FEATURE CLUSTER (V14 vs V10)")
        fig.update_layout(CYBER_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 🌐 Regional Fraud Incident Registry")
    stats = get_country_fraud_stats()
    rows_html = ""
    for row in stats:
        status_badge = '<span class="badge-approved">SECURE</span>' if row['status'] == 'SECURE' else (
            '<span class="badge-review">MONITORED</span>' if row['status'] == 'MONITORED' else '<span class="badge-blocked">ALERT</span>'
        )
        rows_html += f"""
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.95rem;">
            <td style="padding: 12px; font-weight: 700;">{row['flag']} {row['country']}</td>
            <td style="color: #94A3B8;">{row['code']}</td>
            <td>{row['total']}</td>
            <td style="color: #EF4444; font-weight: 700;">{row['fraud']}</td>
            <td style="font-family: monospace;">{row['volume']}</td>
            <td>{status_badge}</td>
        </tr>
        """

    table_html = f"""
    <div style="background: rgba(8, 27, 51, 0.6); border: 1px solid rgba(0, 212, 255, 0.15); border-radius: 16px; padding: 1rem; overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; color: #FFFFFF;">
            <thead>
                <tr style="border-bottom: 1px solid rgba(0, 212, 255, 0.3); color: #00D4FF; font-size: 0.85rem; text-transform: uppercase;">
                    <th style="padding: 12px;">Country / Gateway</th>
                    <th>Code</th>
                    <th>Processed Txns</th>
                    <th>Fraud Cases</th>
                    <th>Total Volume</th>
                    <th>Threat Level</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
    safe_html(table_html)
