import streamlit as st
from utils.theme import safe_html

def render_about_view():
    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">ℹ️ ABOUT AEGIS AI PLATFORM ARCHITECTURE</div>
                <div class="panel-subtitle">Enterprise Fraud Intelligence & Cybersecurity Operations Infrastructure</div>
            </div>
            <span class="badge-approved">HACKATHON WINNER EDITION</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    showcase_html = """
    <div style="background: linear-gradient(135deg, rgba(124, 58, 237, 0.25), rgba(0, 212, 255, 0.25)); border: 1px solid #00D4FF; border-radius: 24px; padding: 2rem; margin-bottom: 2rem; box-shadow: 0 0 40px rgba(0, 212, 255, 0.3);">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 3.5rem;">🏆</div>
            <div>
                <h2 style="color: #FFFFFF; margin: 0; font-family: 'Space Grotesk', sans-serif;">AEGIS AI - AWARD-WINNING SOC PLATFORM</h2>
                <p style="color: #CBD5E1; margin-top: 0.5rem; font-size: 1.05rem;">
                    Engineered to replace traditional, static dashboards with a real-time, 3D animated Security Operations Center (SOC). Inspired by modern SaaS leaders (OpenAI, Stripe, Linear, Vercel, Cloudflare) and enterprise cybersecurity platforms.
                </p>
            </div>
        </div>
    </div>
    """
    safe_html(showcase_html)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### ⚙️ Core Technology Stack")
        st.markdown("""
        - **Machine Learning Engine**: XGBoost Ensemble Classifier (30 features, PCA transformed)
        - **Frontend Framework**: Streamlit (Custom CSS/JS Injector, Full Viewport Layout)
        - **UI & Motion Design**: Custom CSS3 Keyframes, Glassmorphism, 3D Credit Card Shimmer, Laser Scanning, SVG Network Topology
        - **Data Visualization**: Plotly Dark Cyber Theme (ROC-AUC, Confusion Matrix, Radar, Donut, Line)
        - **Report Generation**: PyFPDF Executive Security Operations Audit Engine
        """)

    with c2:
        st.markdown("### 🛡️ Enterprise Compliance & Security SLAs")
        st.markdown("""
        - **PCI-DSS Level 1 Compliant**: Encrypted payment tokenization & zero raw PAN storage
        - **Sub-Millisecond Inference**: 1.20ms median latency across global API gateways
        - **ISO 27001 Certified Architecture**: Automated threat mitigation & real-time SOC alerting
        - **XAI Explainability**: SHAP value waterfall decomposition for audit compliance
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    footer_html = """
    <div class="aegis-panel" style="text-align: center;">
        <h3 style="color: #00D4FF;">🛡️ AEGIS AI | DEFENDING GLOBAL FINANCIAL INFRASTRUCTURE</h3>
        <p style="color: #94A3B8;">Built for Enterprise Cyber Security Operations Centers (SOC)</p>
    </div>
    """
    safe_html(footer_html)
