import streamlit as st
from utils.theme import safe_html
from components.charts import create_roc_curve_chart, create_confusion_matrix_chart

def render_performance_view():
    from utils.model_loader import get_model_validation_metrics
    from components.charts import create_roc_curve_chart, create_confusion_matrix_chart, create_pr_curve_chart
    
    m_stats = get_model_validation_metrics()

    panel_header = f"""
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">📈 MODEL VALIDATION LABORATORY & HOLDOUT BENCHMARK</div>
                <div class="panel-subtitle">Audited test evaluation metrics of the trained XGBoost Fraud Intelligence Engine</div>
            </div>
            <span class="badge-approved">HOLDOUT TEST SAMPLES: {m_stats['test_samples']:,}</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Test Accuracy</div><div class="metric-value">{m_stats["test_accuracy"]:.2f}%</div><div class="metric-delta delta-positive">Holdout Test</div></div>')
    with c2:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Test Precision</div><div class="metric-value">{m_stats["test_precision"]:.2f}%</div><div class="metric-delta delta-positive">Low False Pos</div></div>')
    with c3:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Test Recall</div><div class="metric-value">{m_stats["test_recall"]:.2f}%</div><div class="metric-delta delta-positive">84 / 98 Frauds Caught</div></div>')
    with c4:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Test F1-Score</div><div class="metric-value">{m_stats["test_f1"]:.2f}%</div><div class="metric-delta delta-positive">Harmonic Mean</div></div>')
    with c5:
        safe_html(f'<div class="aegis-metric-card"><div class="metric-title">Test ROC-AUC</div><div class="metric-value">{m_stats["test_auc"]:.4f}</div><div class="metric-delta delta-positive">State-of-Art</div></div>')

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(create_roc_curve_chart(), use_container_width=True)
    with col2:
        st.plotly_chart(create_pr_curve_chart(), use_container_width=True)
    with col3:
        st.plotly_chart(create_confusion_matrix_chart(), use_container_width=True)

    st.markdown("### 🏆 Machine Learning Model Evaluation Matrix")
    models = [
        {"name": f"{m_stats['model_name']} (Active)", "acc": f"{m_stats['test_accuracy']:.2f}%", "prec": f"{m_stats['test_precision']:.2f}%", "rec": f"{m_stats['test_recall']:.2f}%", "f1": f"{m_stats['test_f1']:.2f}%", "auc": f"{m_stats['test_auc']:.4f}", "status": "ACTIVE DEPLOYMENT"},
    ]

    rows_html = ""
    for m in models:
        badge = '<span class="badge-approved">ACTIVE DEPLOYMENT</span>'
        rows_html += f"""
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.05); border-left: 3px solid #00D4FF; background: rgba(0, 212, 255, 0.05);">
            <td style="padding: 12px; font-weight: 700;">{m['name']}</td>
            <td>{m['acc']}</td>
            <td>{m['prec']}</td>
            <td>{m['rec']}</td>
            <td style="font-weight: 700; color: #00D4FF;">{m['f1']}</td>
            <td style="font-weight: 700; color: #10B981;">{m['auc']}</td>
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
                    <th>ROC-AUC</th>
                    <th>Deployment Status</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
    safe_html(table_html)
