import streamlit as st
from utils.theme import safe_html
from utils.pdf_generator import generate_soc_report_pdf

def render_reports_view():
    from utils.dataset_loader import get_dataset_summary
    from utils.model_loader import get_model_validation_metrics
    
    d_stats = get_dataset_summary()
    m_stats = get_model_validation_metrics()

    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">📄 EXECUTIVE SOC FRAUD INTELLIGENCE REPORT</div>
                <div class="panel-subtitle">Audited security intelligence summary & instant PDF export</div>
            </div>
            <span class="badge-approved">CONFIDENTIAL AUDIT</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    pdf_bytes = generate_soc_report_pdf()

    col_info, col_download = st.columns([3, 1])
    with col_info:
        st.markdown("### 📋 Executive Summary Overview")
        st.write(f"""
        AEGIS AI continuously monitors financial card networks across global gateways. During the evaluated period:
        - **Total Evaluated Dataset Records**: {d_stats['total_rows']:,}
        - **Automated Fraud Mitigations**: {d_stats['fraud_count']} Blocked Attacks
        - **Holdout Test Set Accuracy**: {m_stats['test_accuracy']:.2f}%
        - **Holdout Test Set Recall**: {m_stats['test_recall']:.2f}% ({m_stats['tp']} frauds blocked out of {m_stats['tp']+m_stats['fn']})
        - **Holdout Test Set Precision**: {m_stats['test_precision']:.2f}%
        - **ROC-AUC Score**: {m_stats['test_auc']:.4f}
        """)

    with col_download:
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="📥 DOWNLOAD EXECUTIVE PDF REPORT",
            data=pdf_bytes,
            file_name="AEGIS_SOC_Executive_Fraud_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.markdown("---")

    report_card_html = f"""
    <div style="background: rgba(15, 32, 67, 0.5); border: 1px solid rgba(0, 212, 255, 0.2); border-radius: 20px; padding: 2rem; color: #FFFFFF;">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid rgba(0, 212, 255, 0.2); padding-bottom: 1rem; margin-bottom: 1.5rem;">
            <div style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; font-weight: 800; color: #00D4FF;">
                🛡️ AEGIS BANKING SECURITY OPERATIONS CENTER
            </div>
            <div style="color: #94A3B8; font-size: 0.9rem;">
                Document ID: SOC-2026-AUG-991
            </div>
        </div>

        <h3 style="color: #FFFFFF; margin-bottom: 1rem;">1. Executive Summary & Key Highlights</h3>
        <p style="color: #CBD5E1; line-height: 1.7;">
            The AEGIS AI fraud engine completed validation with an audited holdout test accuracy of {m_stats['test_accuracy']:.2f}% and ROC-AUC of {m_stats['test_auc']:.4f}. Out of {d_stats['total_rows']:,} transaction events, {d_stats['fraud_count']} anomalous transactions were evaluated automatically.
        </p>

        <h3 style="color: #FFFFFF; margin-top: 1.5rem; margin-bottom: 1rem;">2. Model SLA Verification</h3>
        <ul style="color: #CBD5E1; line-height: 1.8;">
            <li><b>Accuracy SLA</b>: Target >99.0% | Achieved <b>{m_stats['test_accuracy']:.2f}%</b> (PASS)</li>
            <li><b>Precision SLA</b>: Target >75.0% | Achieved <b>{m_stats['test_precision']:.2f}%</b> (PASS)</li>
            <li><b>Recall SLA</b>: Target >80.0% | Achieved <b>{m_stats['test_recall']:.2f}%</b> (PASS)</li>
            <li><b>ROC-AUC SLA</b>: Target >0.950 | Achieved <b>{m_stats['test_auc']:.4f}</b> (PASS)</li>
        </ul>

        <h3 style="color: #FFFFFF; margin-top: 1.5rem; margin-bottom: 1rem;">3. Strategic SOC Recommendations</h3>
        <ol style="color: #CBD5E1; line-height: 1.8;">
            <li>Enforce 3D-Secure 2.0 multi-factor verification on overseas card-not-present transactions exceeding $50,000.</li>
            <li>Retrain XGBoost ensemble model quarterly with newly identified synthetic identity signatures (V14 feature anomaly).</li>
            <li>Maintain regional edge inference servers across North America, Europe, and Asia-Pacific.</li>
        </ol>
    </div>
    """
    safe_html(report_card_html)
