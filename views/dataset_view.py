import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.theme import safe_html
from utils.dataset_loader import get_sample_dataset, get_country_fraud_stats
from components.charts import create_bar_chart, CYBER_LAYOUT

def render_dataset_view():
    from utils.dataset_loader import get_dataset_summary, get_sample_dataset, get_country_fraud_stats, load_full_dataset
    
    d_stats = get_dataset_summary()

    panel_header = f"""
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">📊 DATA INTELLIGENCE CENTER & AUDIT REGISTRY</div>
                <div class="panel-subtitle">Audited Kaggle European credit card fraud dataset with 28 PCA threat features</div>
            </div>
            <span class="badge-approved">{d_stats['total_rows']:,} SAMPLES VERIFIED</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Total Records</div><div class="metric-value">{d_stats["total_rows"]:,}</div><div class="metric-delta delta-positive">Full History</div></div>')
    with c2:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Fraud Cases</div><div class="metric-value">{d_stats["fraud_count"]}</div><div class="metric-delta delta-negative">{d_stats["fraud_pct"]}% Imbalance</div></div>')
    with c3:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Feature Vectors</div><div class="metric-value">{d_stats["feature_count"]}</div><div class="metric-delta delta-positive">V1 to V28 + Time/Amt</div></div>')
    with c4:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Missing Values</div><div class="metric-value">{d_stats["null_count"]}</div><div class="metric-delta delta-positive">100% Complete</div></div>')
    with c5:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Duplicates</div><div class="metric-value">{d_stats["duplicate_count"]:,}</div><div class="metric-delta delta-neutral">{d_stats["duplicate_pct"]}% Audit Ratio</div></div>')

    st.markdown("<br>", unsafe_allow_html=True)

    # Data Preview Expander & Table
    st.markdown("### 📋 Verified Dataset Preview & Feature Inspection")
    sample_df = get_sample_dataset(100)
    st.dataframe(sample_df, use_container_width=True, height=280)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.plotly_chart(create_bar_chart(), use_container_width=True)
    with col2:
        df = get_sample_dataset(800)
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
