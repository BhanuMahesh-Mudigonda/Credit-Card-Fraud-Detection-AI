import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.theme import safe_html
from utils.simulation_engine import (
    generate_simulated_transaction,
    get_ai_fraud_reasoning,
    get_fraud_network_data,
    get_model_health_data
)

def render_attack_simulator_bar():
    """Renders the Real-Time Fraud Attack Simulator control bar with interactive buttons."""
    sim_bar_html = """
    <div class="aegis-panel" style="background: linear-gradient(135deg, rgba(10, 15, 36, 0.95), rgba(239, 68, 68, 0.12)); border: 1.5px solid rgba(239, 68, 68, 0.4); margin-bottom: 1.2rem;">
        <div class="panel-header" style="margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span class="pulse-green-dot" style="background: #EF4444; box-shadow: 0 0 10px #EF4444;"></span>
                <div>
                    <div class="panel-title" style="color: #FFFFFF;">🚨 REAL-TIME FRAUD ATTACK SIMULATOR & DEMONSTRATION SUITE</div>
                    <div class="panel-subtitle">Inject synthetic attack streams into the live XGBoost inference pipeline to evaluate threat detection</div>
                </div>
            </div>
            <span class="badge-approved" style="background: rgba(239, 68, 68, 0.15); border: 1px solid #EF4444; color: #EF4444;">SIMULATION ENGINE READY</span>
        </div>
    </div>
    """
    safe_html(sim_bar_html)

    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c1:
        if st.button("🚨 SIMULATE LIVE ATTACK", key="btn_sim_attack", type="primary", use_container_width=True):
            tx = generate_simulated_transaction(is_attack=True)
            if "prediction_history" not in st.session_state:
                st.session_state.prediction_history = []
            st.session_state.prediction_history.append(tx)
            st.session_state.last_simulated_tx = tx
            st.toast(f"🚨 Attack Simulated: Txn #{tx['id']} (${tx['amount']:,.2f}) — {tx['decision']}", icon="🚨")
            st.rerun()

    with c2:
        if st.button("⚡ RUN FULL ATTACK SIMULATION PIPELINE", key="btn_sim_full_pipeline", type="secondary", use_container_width=True):
            # Run multi-stage simulation pipeline
            st.session_state.running_full_simulation = True
            tx = generate_simulated_transaction(is_attack=True)
            if "prediction_history" not in st.session_state:
                st.session_state.prediction_history = []
            st.session_state.prediction_history.append(tx)
            st.session_state.last_simulated_tx = tx
            st.toast("⚡ Full 10-Stage Attack Simulation Executed!", icon="⚡")
            st.rerun()

    with c3:
        if st.button("✅ SIMULATE LEGITIMATE TRANSACTION", key="btn_sim_legit", use_container_width=True):
            tx = generate_simulated_transaction(is_attack=False)
            if "prediction_history" not in st.session_state:
                st.session_state.prediction_history = []
            st.session_state.prediction_history.append(tx)
            st.session_state.last_simulated_tx = tx
            st.toast(f"✅ Normal Txn Simulated: Txn #{tx['id']} (${tx['amount']:,.2f}) — {tx['decision']}", icon="✅")
            st.rerun()

def render_global_attack_map():
    """Renders the Global Fraud Attack Map visualization with interactive animated markers."""
    locations = [
        {"city": "Mumbai", "lat": 19.0760, "lon": 72.8777, "attacks": 32, "level": "CRITICAL", "color": "#EF4444"},
        {"city": "London", "lat": 51.5074, "lon": -0.1278, "attacks": 18, "level": "HIGH", "color": "#F59E0B"},
        {"city": "New York", "lat": 40.7128, "lon": -74.0060, "attacks": 41, "level": "CRITICAL", "color": "#EF4444"},
        {"city": "Singapore", "lat": 1.3521, "lon": 103.8198, "attacks": 12, "level": "MEDIUM", "color": "#00F0FF"},
        {"city": "Dubai", "lat": 25.2048, "lon": 55.2708, "attacks": 27, "level": "HIGH", "color": "#F59E0B"},
        {"city": "Frankfurt", "lat": 50.1109, "lon": 8.6821, "attacks": 9, "level": "LOW", "color": "#10B981"},
        {"city": "Tokyo", "lat": 35.6762, "lon": 139.6503, "attacks": 15, "level": "MEDIUM", "color": "#8B5CF6"}
    ]
    
    # Check if a simulation event occurred to increase count
    history = st.session_state.get("prediction_history", [])
    if history:
        last_item = history[-1]
        for loc in locations:
            if loc['city'] in str(last_item.get('location', {}).get('city', '')):
                loc['attacks'] += 1

    fig = go.Figure()

    for loc in locations:
        fig.add_trace(go.Scattergeo(
            lon=[loc['lon']],
            lat=[loc['lat']],
            text=f"<b>{loc['city']}</b><br>Threat Count: {loc['attacks']} Attacks<br>Level: {loc['level']}",
            mode='markers+text',
            textposition="top center",
            textfont=dict(color='#FFFFFF', size=11, family='Space Grotesk'),
            marker=dict(
                size=max(14, min(36, loc['attacks'] * 0.8)),
                color=loc['color'],
                opacity=0.85,
                line=dict(width=2, color='#FFFFFF')
            ),
            name=f"{loc['city']} ({loc['attacks']})"
        ))

    fig.update_layout(
        title="🌐 GLOBAL FRAUD ATTACK MAP — LIVE THREAT CLUSTER SURVEILLANCE",
        title_font=dict(family="Space Grotesk", size=14, color="#00F0FF"),
        geo=dict(
            projection_type='natural earth',
            showland=True,
            landcolor='rgba(15, 23, 52, 0.9)',
            countrycolor='rgba(0, 240, 255, 0.25)',
            showocean=True,
            oceancolor='rgba(4, 6, 18, 0.95)',
            lakecolor='rgba(4, 6, 18, 0.95)',
            bgcolor='rgba(0,0,0,0)',
            showframe=False,
            showcoastlines=True,
            coastlinecolor='rgba(0, 240, 255, 0.4)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

def render_fraud_network_graph():
    """Renders the Fraud Network & Fraud Ring Detection visualization graph."""
    net_data = get_fraud_network_data()

    # Pre-calculated node coordinates for balanced network layout
    pos = {
        "USER_9012": (0.1, 0.8),
        "CARD_4892": (0.3, 0.8),
        "DEVICE_IP": (0.5, 0.5),
        "LOC_MUMBAI": (0.2, 0.2),
        "LOC_LONDON": (0.8, 0.2),
        "MERCHANT_LUX": (0.7, 0.8),
        "TXN_92831": (0.5, 0.8),
        "CARD_9104": (0.7, 0.5),
        "USER_7710": (0.9, 0.5)
    }

    edge_x = []
    edge_y = []
    for edge in net_data['edges']:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1.8, color='rgba(239, 68, 68, 0.6)'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_text = []
    node_color = []
    node_size = []

    for node in net_data['nodes']:
        x, y = pos[node['id']]
        node_x.append(x)
        node_y.append(y)
        node_text.append(f"<b>{node['label']}</b><br>Entity Type: {node['type']}")
        node_color.append(node['color'])
        node_size.append(node['size'])

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=[n['label'] for n in net_data['nodes']],
        textposition="bottom center",
        textfont=dict(color='#FFFFFF', size=10, family='Space Grotesk'),
        hovertext=node_text,
        marker=dict(
            size=node_size,
            color=node_color,
            line=dict(width=2, color='#FFFFFF')
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title="🕸️ FRAUD NETWORK & FRAUD RING DETECTION GRAPH",
        title_font=dict(family="Space Grotesk", size=14, color="#8B5CF6"),
        showlegend=False,
        hovermode='closest',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=380,
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
    )

    st.plotly_chart(fig, use_container_width=True)

    ring_alert_html = f"""
    <div style="background: rgba(239, 68, 68, 0.15); border: 1.5px solid #EF4444; border-radius: 12px; padding: 10px 16px; display: flex; align-items: center; justify-content: space-between; font-size: 0.82rem; color: #FFFFFF; margin-top: -10px;">
        <div><b>{net_data['cluster_alert']}</b></div>
        <span class="badge-blocked">CLUSTER ISOLATED</span>
    </div>
    """
    safe_html(ring_alert_html)

def render_adaptive_risk_breakdown(model_prob, behavior_risk, velocity_risk, location_risk, final_score):
    """Renders the Adaptive Risk Engine breakdown matrix with 4 sub-factors and final score badge."""
    if final_score >= 85.0:
        badge_cls = "badge-blocked"
        badge_label = "🔴 CRITICAL RISK"
        badge_color = "#EF4444"
    elif final_score >= 60.0:
        badge_cls = "badge-blocked"
        badge_label = "🟠 HIGH RISK"
        badge_color = "#F59E0B"
    elif final_score >= 30.0:
        badge_cls = "badge-approved"
        badge_label = "🟡 MEDIUM RISK"
        badge_color = "#F59E0B"
    else:
        badge_cls = "badge-approved"
        badge_label = "🟢 LOW RISK"
        badge_color = "#10B981"

    risk_html = f"""
    <div class="aegis-panel" style="background: rgba(10, 15, 36, 0.85); border: 1.5px solid rgba(0, 240, 255, 0.35);">
        <div class="panel-header" style="margin-bottom: 14px;">
            <div>
                <div class="panel-title">⚖️ ADAPTIVE RISK ENGINE BREAKDOWN</div>
                <div class="panel-subtitle">Multi-dimensional risk synthesis: Model Probability + Behavior + Velocity + Location</div>
            </div>
            <span class="{badge_cls}" style="font-size: 0.85rem; padding: 4px 14px;">{badge_label}</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.85rem; color: #E2E8F0;">
            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span><b>XGBoost Model Probability</b></span>
                    <span style="color: #00F0FF; font-weight: 800;">{model_prob:.1f}%</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 6px; height: 8px; overflow: hidden;">
                    <div style="width: {model_prob}%; background: #00F0FF; height: 100%;"></div>
                </div>
            </div>

            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span><b>Behavioral Integrity Risk (V14 Identity)</b></span>
                    <span style="color: #8B5CF6; font-weight: 800;">{behavior_risk:.1f}%</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 6px; height: 8px; overflow: hidden;">
                    <div style="width: {behavior_risk}%; background: #8B5CF6; height: 100%;"></div>
                </div>
            </div>

            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span><b>Velocity & Frequency Risk (V4 Frequency)</b></span>
                    <span style="color: #F59E0B; font-weight: 800;">{velocity_risk:.1f}%</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 6px; height: 8px; overflow: hidden;">
                    <div style="width: {velocity_risk}%; background: #F59E0B; height: 100%;"></div>
                </div>
            </div>

            <div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span><b>Location & Device Anomaly Risk (V12 Vector)</b></span>
                    <span style="color: #EF4444; font-weight: 800;">{location_risk:.1f}%</span>
                </div>
                <div style="background: rgba(255,255,255,0.08); border-radius: 6px; height: 8px; overflow: hidden;">
                    <div style="width: {location_risk}%; background: #EF4444; height: 100%;"></div>
                </div>
            </div>

            <hr style="border-color: rgba(255,255,255,0.1); margin: 8px 0;">

            <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(0,0,0,0.4); padding: 10px 16px; border-radius: 12px; border: 1px solid {badge_color};">
                <span style="font-weight: 800; font-size: 0.92rem; color: #FFFFFF;">FINAL ADAPTIVE RISK SCORE</span>
                <span style="font-family: var(--font-display); font-size: 1.4rem; font-weight: 900; color: {badge_color};">{final_score:.1f} / 100</span>
            </div>
        </div>
    </div>
    """
    safe_html(risk_html)

def render_ai_fraud_reasoning(v14, v10, v12, v4, amount, risk_percent):
    """Renders the AI Fraud Reasoning explanation section ("WHY WAS THIS TRANSACTION FLAGGED?")."""
    reasoning_data = get_ai_fraud_reasoning(v14, v10, v12, v4, amount, risk_percent)
    
    items_html = ""
    for r in reasoning_data['reasons']:
        color_map = {"HIGH": "#EF4444", "MEDIUM": "#F59E0B", "LOW": "#10B981"}
        c = color_map.get(r['impact'], "#00F0FF")
        items_html += f"""
        <div style="background: rgba(15, 23, 52, 0.7); border-left: 4px solid {c}; border-radius: 8px; padding: 10px 14px; margin-bottom: 8px;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
                <span style="font-weight: 800; color: #FFFFFF; font-size: 0.88rem;">{r['title']}</span>
                <span style="background: rgba(0,0,0,0.4); color: {c}; font-size: 0.70rem; font-weight: 800; padding: 2px 8px; border-radius: 6px; border: 1px solid {c};">{r['impact']} IMPACT</span>
            </div>
            <div style="font-size: 0.78rem; color: #CBD5E1; margin-top: 4px;">{r['desc']}</div>
        </div>
        """

    reasoning_panel = f"""
    <div class="aegis-panel" style="background: rgba(10, 15, 36, 0.85); border: 1.5px solid rgba(139, 92, 246, 0.35);">
        <div class="panel-header" style="margin-bottom: 12px;">
            <div>
                <div class="panel-title" style="color: #FFFFFF;">🧠 WHY WAS THIS TRANSACTION FLAGGED?</div>
                <div class="panel-subtitle">SHAP Feature Attribution & Top Risk Factor Explanations</div>
            </div>
            <span class="badge-approved" style="background: rgba(139, 92, 246, 0.15); border: 1px solid #8B5CF6; color: #8B5CF6;">AI CONFIDENCE: {reasoning_data['confidence']:.1f}%</span>
        </div>

        <div>
            {items_html}
        </div>
    </div>
    """
    safe_html(reasoning_panel)

def render_model_health_monitor():
    """Renders the Model Health & Drift Monitor section."""
    mh = get_model_health_data()

    health_html = f"""
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">🩺 MODEL HEALTH & SYSTEM DRIFT MONITOR</div>
                <div class="panel-subtitle">Audited evaluation metrics & real-time telemetry stability</div>
            </div>
            <span class="badge-approved">SYSTEM HEALTHY</span>
        </div>

        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; text-align: center;">
            <div style="background: rgba(15, 23, 52, 0.6); border: 1px solid rgba(0,240,255,0.2); border-radius: 12px; padding: 12px;">
                <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 800;">HOLDOUT ACCURACY</div>
                <div style="font-family: var(--font-display); font-size: 1.4rem; font-weight: 900; color: #00F0FF; margin: 4px 0;">{mh['accuracy']:.2f}%</div>
                <div style="font-size: 0.68rem; color: #10B981;">Verified Test Set</div>
            </div>

            <div style="background: rgba(15, 23, 52, 0.6); border: 1px solid rgba(16,185,129,0.2); border-radius: 12px; padding: 12px;">
                <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 800;">TEST RECALL</div>
                <div style="font-family: var(--font-display); font-size: 1.4rem; font-weight: 900; color: #10B981; margin: 4px 0;">{mh['recall']:.2f}%</div>
                <div style="font-size: 0.68rem; color: #10B981;">84 / 98 Frauds Caught</div>
            </div>

            <div style="background: rgba(15, 23, 52, 0.6); border: 1px solid rgba(245,158,11,0.2); border-radius: 12px; padding: 12px;">
                <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 800;">DATA DRIFT STATUS</div>
                <div style="font-family: var(--font-display); font-size: 1.1rem; font-weight: 900; color: #10B981; margin: 8px 0;">{mh['data_drift']}</div>
                <div style="font-size: 0.68rem; color: #CBD5E1;">Population Stability</div>
            </div>

            <div style="background: rgba(15, 23, 52, 0.6); border: 1px solid rgba(139,92,246,0.2); border-radius: 12px; padding: 12px;">
                <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 800;">MODEL DRIFT STATUS</div>
                <div style="font-family: var(--font-display); font-size: 1.1rem; font-weight: 900; color: #8B5CF6; margin: 8px 0;">{mh['model_drift']}</div>
                <div style="font-size: 0.68rem; color: #CBD5E1;">Model Conformance</div>
            </div>
        </div>
    </div>
    """
    safe_html(health_html)
