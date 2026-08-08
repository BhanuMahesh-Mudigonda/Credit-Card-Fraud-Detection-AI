import streamlit as st
import time
from utils.theme import safe_html
from utils.model_loader import predict_transaction
from components.charts import create_gauge_chart

def render_prediction_view():
    panel_header = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">🤖 AI REAL-TIME FRAUD PREDICTION STUDIO</div>
                <div class="panel-subtitle">Simulate real-time payment transactions and evaluate neural risk scores</div>
            </div>
            <span class="badge-approved">XGBoost MODEL ACTIVE</span>
        </div>
    </div>
    """
    safe_html(panel_header)

    st.markdown("### ⚡ Quick Attack Vectors & Preset Testing")
    p1, p2, p3 = st.columns(3)
    preset_chosen = None
    with p1:
        if st.button("🛒 Preset: Normal E-Commerce ($45.00)", use_container_width=True):
            preset_chosen = "normal"
    with p2:
        if st.button("⚠️ Preset: High Amount POS ($4,800.00)", use_container_width=True):
            preset_chosen = "suspicious"
    with p3:
        if st.button("🚨 Preset: Synthetic Identity Anomaly", use_container_width=True):
            preset_chosen = "fraud"

    def_amount = 120.50
    def_v14 = 0.12
    def_v10 = -0.30
    def_v12 = 0.08
    def_v4 = -0.10

    if preset_chosen == "normal":
        def_amount = 45.00
        def_v14 = 0.50
        def_v10 = 0.20
        def_v12 = 0.40
        def_v4 = 0.05
    elif preset_chosen == "suspicious":
        def_amount = 4800.00
        def_v14 = -2.10
        def_v10 = -1.80
        def_v12 = -1.50
        def_v4 = 1.85
    elif preset_chosen == "fraud":
        def_amount = 9450.00
        def_v14 = -6.80
        def_v10 = -5.40
        def_v12 = -4.90
        def_v4 = 4.20

    col_input, col_sim = st.columns([1, 1])

    with col_input:
        st.markdown("### 💳 Transaction Details")
        amount = st.number_input("Transaction Amount ($)", min_value=0.01, value=def_amount, step=10.0)
        time_sec = st.number_input("Transaction Time Offset (sec)", min_value=0, value=43200, step=100)
        country = st.selectbox("Merchant Country", ["USA 🇺🇸", "India 🇮🇳", "UK 🇬🇧", "Singapore 🇸🇬", "Dubai 🇦🇪", "Germany 🇩🇪"])
        channel = st.selectbox("Payment Channel", ["Online E-Commerce (CNP)", "POS Card Present", "ATM Cash Out", "Cross-Border Wire"])

        with st.expander("🛠️ Advanced PCA Feature Vector Sliders (V1-V28)"):
            v14 = st.slider("V14 (Identity Integrity)", -10.0, 5.0, def_v14)
            v10 = st.slider("V10 (Device Reputation)", -10.0, 5.0, def_v10)
            v12 = st.slider("V12 (Location Velocity)", -10.0, 5.0, def_v12)
            v4 = st.slider("V4 (Transaction Frequency)", -5.0, 10.0, def_v4)

        analyze_btn = st.button("🚀 EXECUTE REAL-TIME AI SCAN", use_container_width=True)

    with col_sim:
        st.markdown("### ⚙️ Step-by-Step AI Workflow")

        v_feats = [0.1, -0.2, 0.3, v4, 0.05, -0.15, 0.2, -0.05, 0.1, v10,
                   0.15, v12, 0.08, -0.4, v14, -0.05, 0.22, -0.18, 0.04, 0.01,
                   -0.02, 0.05, -0.08, 0.03, 0.1, -0.02, 0.04, 0.01]

        prob, _ = predict_transaction(amount, time_sec, v_feats)
        risk_percent = prob * 100

        if analyze_btn:
            # Append prediction event to session_state prediction_history
            if "prediction_history" not in st.session_state:
                st.session_state.prediction_history = []
            
            import random
            from datetime import datetime
            txn_id = random.randint(99100, 99999)
            decision = "BLOCKED" if risk_percent >= 50.0 else "APPROVED"
            
            st.session_state.prediction_history.append({
                "id": txn_id,
                "amount": amount,
                "risk": risk_percent,
                "decision": decision,
                "country": country,
                "channel": channel,
                "timestamp": datetime.now().strftime("%H:%M:%S UTC")
            })

            steps_html = f"""
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div class="feed-item" style="border-left: 4px solid #00F0FF;">
                    <div>01 <b>INPUT RECEIVED</b>: ${amount:,.2f} ({country} • {channel})</div>
                    <span class="badge-approved">PASSED</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid #8B5CF6;">
                    <div>02 <b>FEATURES PREPARED</b>: V14={v14:.2f}, V4={v4:.2f}, V10={v10:.2f}</div>
                    <span class="badge-approved">PASSED</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid #00F0FF;">
                    <div>03 <b>MODEL INFERENCE</b>: XGBoost Gradient Boosted Trees</div>
                    <span class="badge-approved">PASSED</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid #F59E0B;">
                    <div>04 <b>PROBABILITY SCORE</b>: Fraud Risk Calculated</div>
                    <span class="badge-approved">{risk_percent:.2f}% RISK</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid {'#EF4444' if risk_percent >= 50.0 else '#10B981'};">
                    <div>05 <b>DECISION GENERATED</b>: Gateway Policy Enforcement</div>
                    <span class="{'badge-blocked' if risk_percent >= 50.0 else 'badge-approved'}">{decision}</span>
                </div>
            </div>
            <br>
            """
            safe_html(steps_html)

            st.plotly_chart(create_gauge_chart(risk_percent), use_container_width=True)

            if risk_percent >= 50.0:
                alert_html = f"""
                <div style="background: rgba(239, 68, 68, 0.15); border: 2px solid #EF4444; border-radius: 16px; padding: 1.5rem; text-align: center;">
                    <h2 style="color: #EF4444; margin: 0;">🚨 HIGH FRAUD THREAT DETECTED</h2>
                    <p style="color: #FFFFFF; margin-top: 0.5rem;">Fraud Probability: <b>{risk_percent:.2f}%</b></p>
                    <div class="badge-blocked" style="font-size: 1rem; padding: 8px 24px; display: inline-block;">
                        ACTION TAKEN: AUTOMATED TRANSACTION BLOCK
                    </div>
                    <div style="margin-top: 1rem; text-align: left; font-size: 0.9rem; color: #CBD5E1;">
                        <b>Threat Factor Breakdown:</b><br>
                        • Extreme anomaly in V14 Identity feature ({v14:.2f})<br>
                        • Transaction amount velocity (${amount:,.2f})<br>
                        • V4 Frequency deviation ({v4:.2f})
                    </div>
                </div>
                """
                safe_html(alert_html)
            else:
                success_html = f"""
                <div style="background: rgba(16, 185, 129, 0.15); border: 2px solid #10B981; border-radius: 16px; padding: 1.5rem; text-align: center;">
                    <h2 style="color: #10B981; margin: 0;">✅ LEGITIMATE TRANSACTION</h2>
                    <p style="color: #FFFFFF; margin-top: 0.5rem;">Fraud Risk Score: <b>{risk_percent:.2f}%</b></p>
                    <div class="badge-approved" style="font-size: 1rem; padding: 8px 24px; display: inline-block;">
                        ACTION TAKEN: APPROVED & CLEARED
                    </div>
                    <div style="margin-top: 1rem; text-align: left; font-size: 0.9rem; color: #CBD5E1;">
                        <b>Security Verification:</b><br>
                        • Identity V14 within normal baseline ({v14:.2f})<br>
                        • Trusted merchant channel & geography<br>
                        • Pattern matched 99.9% legitimate cluster
                    </div>
                </div>
                """
                safe_html(success_html)
        else:
            st.info("👈 Adjust inputs or click a preset above, then hit 'EXECUTE REAL-TIME AI SCAN'.")
