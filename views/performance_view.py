import streamlit as st
from utils.theme import safe_html
from components.charts import create_roc_curve_chart, create_confusion_matrix_chart

def render_performance_view():
    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">📈 MODEL PERFORMANCE & SOC BENCHMARK</div>
                <div class="panel-subtitle">Comprehensive evaluation metrics of the deployed XGBoost Fraud Intelligence Engine</div>
            </div>
            <span class="badge-approved">MODEL ACCURACY 99.95%</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">Accuracy</div><div class="metric-value">99.95%</div><div class="metric-delta delta-positive">SLA >99.5%</div></div>')
    with c2:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">Precision</div><div class="metric-value">98.40%</div><div class="metric-delta delta-positive">Low False Pos</div></div>')
    with c3:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">Recall</div><div class="metric-value">89.20%</div><div class="metric-delta delta-positive">Catch Rate</div></div>')
    with c4:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">F1-Score</div><div class="metric-value">93.55%</div><div class="metric-delta delta-positive">Optimal Balance</div></div>')
    with c5:
        safe_html('<div class="aegis-metric-card"><div class="metric-title">ROC-AUC</div><div class="metric-value">0.9972</div><div class="metric-delta delta-positive">State-of-Art</div></div>')

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(create_roc_curve_chart(), use_container_width=True)
    with col2:
        st.plotly_chart(create_confusion_matrix_chart(), use_container_width=True)

    st.markdown("### 🏆 Machine Learning Model Benchmark Matrix")
    models = [
        {"name": "AEGIS XGBoost Ensemble (Active)", "acc": "99.95%", "prec": "98.40%", "rec": "89.20%", "f1": "93.55%", "lat": "1.20 ms", "status": "ACTIVE DEPLOYMENT"},
        {"name": "Random Forest Classifier", "acc": "99.93%", "prec": "96.10%", "rec": "85.40%", "f1": "90.41%", "lat": "4.80 ms", "status": "STANDBY"},
        {"name": "Deep Neural Network (MLP)", "acc": "99.91%", "prec": "93.50%", "rec": "82.10%", "f1": "87.43%", "lat": "8.50 ms", "status": "EXPERIMENTAL"},
        {"name": "Logistic Regression Baseline", "acc": "99.88%", "prec": "86.20%", "rec": "62.40%", "f1": "72.40%", "lat": "0.40 ms", "status": "LEGACY"},
    ]

    rows_html = ""
    for m in models:
        is_active = "border-left: 3px solid #00D4FF; background: rgba(0, 212, 255, 0.05);" if "Active" in m['name'] else ""
        badge = '<span class="badge-approved">ACTIVE</span>' if "ACTIVE" in m['status'] else '<span class="badge-review">STANDBY</span>'
        rows_html += f"""
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05); {is_active}">
            <td style="padding: 12px; font-weight: 700;">{m['name']}</td>
            <td>{m['acc']}</td>
            <td>{m['prec']}</td>
            <td>{m['rec']}</td>
            <td style="font-weight: 700; color: #00D4FF;">{m['f1']}</td>
            <td>{m['lat']}</td>
            <td>{badge}</td>
        </tr>
        """

    table_html = f"""
    <div style="background: rgba(8, 27, 51, 0.6); border: 1px solid rgba(0, 212, 255, 0.15); border-radius: 16px; padding: 1rem;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; color: #FFFFFF;">
            <thead>
                <tr style="border-bottom: 1px solid rgba(0, 212, 255, 0.3); color: #00D4FF; font-size: 0.85rem;">
                    <th style="padding: 12px;">Model Architecture</th>
                    <th>Accuracy</th>
                    <th>Precision</th>
                    <th>Recall</th>
                    <th>F1-Score</th>
                    <th>Latency</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
    safe_html(table_html)
