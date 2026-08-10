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
    # Render Real-Time Fraud Attack Simulator Bar
    from components.soc_intelligence import (
        render_attack_simulator_bar,
        render_adaptive_risk_breakdown,
        render_ai_fraud_reasoning
    )
    render_attack_simulator_bar()

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

        if analyze_btn or "last_simulated_tx" in st.session_state:
            # Handle prediction or simulation result
            if analyze_btn:
                import random
                from datetime import datetime
                txn_id = f"TX-{random.randint(99100, 99999)}"
                decision = "BLOCKED" if risk_percent >= 50.0 else "APPROVED"
                
                sim_event = {
                    "id": txn_id,
                    "amount": amount,
                    "risk": risk_percent,
                    "decision": decision,
                    "country": country,
                    "channel": channel,
                    "timestamp": datetime.now().strftime("%H:%M:%S UTC"),
                    "v14": v14, "v10": v10, "v12": v12, "v4": v4,
                    "model_prob_pct": round(risk_percent, 2),
                    "behavior_risk": round(min(100.0, max(5.0, (abs(v14) * 12.0))), 1),
                    "velocity_risk": round(min(100.0, max(5.0, (v4 * 15.0) + (amount / 200.0))), 1),
                    "location_risk": round(min(100.0, max(5.0, (abs(v12) * 14.0))), 1),
                    "final_risk_score": round(risk_percent, 1)
                }
                st.session_state.last_simulated_tx = sim_event
                if "prediction_history" not in st.session_state:
                    st.session_state.prediction_history = []
                st.session_state.prediction_history.append(sim_event)
            else:
                sim_event = st.session_state.last_simulated_tx

            cur_amount = sim_event.get('amount', amount)
            cur_risk = sim_event.get('final_risk_score', risk_percent)
            cur_decision = sim_event.get('decision', 'BLOCKED' if cur_risk >= 50 else 'APPROVED')

            steps_html = f"""
            <div style="display: flex; flex-direction: column; gap: 8px;">
                <div class="feed-item" style="border-left: 4px solid #00F0FF;">
                    <div>01 <b>INPUT RECEIVED</b>: ${cur_amount:,.2f} ({sim_event.get('country', country)} • {sim_event.get('channel', channel)})</div>
                    <span class="badge-approved">PASSED</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid #8B5CF6;">
                    <div>02 <b>FEATURES PREPARED</b>: V14={sim_event.get('v14', v14):.2f}, V4={sim_event.get('v4', v4):.2f}, V10={sim_event.get('v10', v10):.2f}</div>
                    <span class="badge-approved">PASSED</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid #00F0FF;">
                    <div>03 <b>MODEL INFERENCE</b>: XGBoost Gradient Boosted Trees</div>
                    <span class="badge-approved">PASSED</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid #F59E0B;">
                    <div>04 <b>PROBABILITY SCORE</b>: Fraud Risk Calculated</div>
                    <span class="badge-approved">{cur_risk:.2f}% RISK</span>
                </div>
                <div class="feed-item" style="border-left: 4px solid {'#EF4444' if cur_risk >= 50.0 else '#10B981'};">
                    <div>05 <b>DECISION GENERATED</b>: Gateway Policy Enforcement</div>
                    <span class="{'badge-blocked' if cur_risk >= 50.0 else 'badge-approved'}">{cur_decision}</span>
                </div>
            </div>
            <br>
            """
            safe_html(steps_html)

            st.plotly_chart(create_gauge_chart(cur_risk), use_container_width=True)

            # Render Adaptive Risk Breakdown & AI Reasoning
            render_adaptive_risk_breakdown(
                model_prob=sim_event.get('model_prob_pct', cur_risk),
                behavior_risk=sim_event.get('behavior_risk', 50.0),
                velocity_risk=sim_event.get('velocity_risk', 50.0),
                location_risk=sim_event.get('location_risk', 50.0),
                final_score=cur_risk
            )

            render_ai_fraud_reasoning(
                v14=sim_event.get('v14', v14),
                v10=sim_event.get('v10', v10),
                v12=sim_event.get('v12', v12),
                v4=sim_event.get('v4', v4),
                amount=cur_amount,
                risk_percent=cur_risk
            )

            # Impossible Travel Detection Banner if present
            imp_travel = sim_event.get('impossible_travel')
            if imp_travel:
                travel_html = f"""
                <div style="background: rgba(239, 68, 68, 0.18); border: 2px solid #EF4444; border-radius: 14px; padding: 12px 18px; margin-top: 10px;">
                    <div style="color: #EF4444; font-weight: 800; font-size: 0.92rem;">{imp_travel['status']}</div>
                    <div style="font-size: 0.82rem; color: #FFFFFF; margin-top: 4px;">
                        Previous: <b>{imp_travel['prev_location']}</b> ➔ Current: <b>{imp_travel['curr_location']}</b> (Elapsed: {imp_travel['time_diff_mins']} mins)
                    </div>
                </div>
                """
                safe_html(travel_html)

            if st.button("📄 GENERATE & VIEW INCIDENT REPORT", key="btn_gen_report_pred", use_container_width=True):
                st.session_state.current_page = "Reports"
                st.rerun()

        else:
            st.info("👈 Adjust inputs, click a preset, or click '🚨 SIMULATE LIVE ATTACK' above to run the live scan.")
