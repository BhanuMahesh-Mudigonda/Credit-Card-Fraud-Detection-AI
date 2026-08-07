import streamlit as st
from utils.theme import safe_html
from components.live_feed import render_world_network, render_live_feed
from components.charts import create_line_chart

def render_dashboard_view():
    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">📡 SOC LIVE MONITORING COMMAND CENTER</div>
                <div class="panel-subtitle">Real-time global transaction streaming feed & threat surveillance console</div>
            </div>
            <span class="badge-approved">STREAM ACTIVE | 12.4K TPS</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">Live Throughput</div><div class="metric-value">12,480 /s</div><div class="metric-delta delta-positive">Peak Capacity 50K</div></div>')
    with c2:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">Threat Velocity</div><div class="metric-value">4.2 /min</div><div class="metric-delta delta-negative">Controlled</div></div>')
    with c3:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">Auto-Block Rate</div><div class="metric-value">100.0%</div><div class="metric-delta delta-positive">Zero Leaks</div></div>')
    with c4:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">System Health</div><div class="metric-value">99.999%</div><div class="metric-delta delta-positive">All Nodes Green</div></div>')

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        render_world_network()
    with col2:
        render_live_feed()

    st.plotly_chart(create_line_chart(), use_container_width=True)

    st.markdown("### 🖥️ Security Operations Center Live Audit Logs")
    logs_html = """
    <div style="background: #030612; border: 1px solid rgba(0, 212, 255, 0.2); border-radius: 16px; padding: 1.2rem; font-family: monospace; font-size: 0.85rem; color: #4ADE80; max-height: 250px; overflow-y: auto;">
        <div>[20:14:02.102 UTC] [INFO] [AEGIS-NODE-IN] Ingested Txn #991041 | Amt: ₹25,000 | Risk: 1.2% -> <span style="color: #4ADE80;">APPROVED</span></div>
        <div>[20:14:03.450 UTC] [WARN] [AEGIS-NODE-US] Ingested Txn #991042 | Amt: $1,150.00 | Risk: 96.8% -> <span style="color: #EF4444;">BLOCKED (RULE: V14_ANOMALY)</span></div>
        <div>[20:14:04.890 UTC] [INFO] [AEGIS-NODE-JP] Ingested Txn #991043 | Amt: ¥450,000 | Risk: 62.1% -> <span style="color: #F59E0B;">FLAGGED_REVIEW</span></div>
        <div>[20:14:06.120 UTC] [INFO] [AEGIS-NODE-DE] Ingested Txn #991044 | Amt: €12,500 | Risk: 0.8% -> <span style="color: #4ADE80;">APPROVED</span></div>
        <div>[20:14:09.300 UTC] [CRIT] [AEGIS-NODE-AE] Ingested Txn #991045 | Amt: $45,000.00 | Risk: 99.4% -> <span style="color: #EF4444;">BLOCKED (RULE: SYNTHETIC_IDENTITY)</span></div>
        <div>[20:14:12.010 UTC] [INFO] [AEGIS-NODE-GB] Ingested Txn #991046 | Amt: £8,200 | Risk: 2.1% -> <span style="color: #4ADE80;">APPROVED</span></div>
    </div>
    """
    safe_html(logs_html)
