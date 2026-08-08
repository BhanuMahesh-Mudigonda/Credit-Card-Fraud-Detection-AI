import streamlit as st
from utils.theme import safe_html
from utils.dataset_loader import get_dataset_summary
from utils.model_loader import get_model_validation_metrics

def render_landing_hero():
    d_stats = get_dataset_summary()
    m_stats = get_model_validation_metrics()

    hero_left_html = f"""
    <div class="hero-left-column slow-motion-cinematic">
        <div class="hero-pill-tag">
            <span class="pulse-green-dot"></span>
            <span>GLOBAL FINTECH PROTECTION • SUB-MS AI SCAN</span>
        </div>

        <h1 class="hero-main-title">
            🛡️ AEGIS AI <br>
            <span class="gradient-text-hero">NEXT-GEN 3D</span> <br>
            FRAUD INTELLIGENCE
        </h1>

        <p class="hero-main-subtitle">
            Autonomous AI protecting global payment card networks, digital wallets, crypto assets, and banking wire transfers in real time with sub-millisecond XGBoost threat scoring.
        </p>

        <!-- Global Threat Network Status Strip -->
        <div class="aegis-global-status-strip">
            <span class="global-status-title">GLOBAL THREAT NETWORK</span>
            <div class="global-status-items">
                <span class="status-item"><span class="status-dot green-dot"></span> MODEL ONLINE</span>
                <span class="status-item"><span class="status-dot cyan-dot"></span> FEATURE SPACE ACTIVE</span>
                <span class="status-item"><span class="status-dot amber-dot"></span> RISK SCORING READY</span>
                <span class="status-item"><span class="status-dot violet-dot"></span> SHAP EXPLANATION READY</span>
            </div>
        </div>

        <!-- Technical Status Strip inside Hero -->
        <div class="aegis-hero-status-strip">
            <div class="status-strip-header">
                <span class="status-strip-dot"></span>
                <span>AEGIS INFERENCE CORE ARCHITECTURE</span>
            </div>
            <div class="status-strip-flow">
                <span class="flow-node">PAYLOAD</span>
                <span class="flow-arrow">➔</span>
                <span class="flow-node">V1–V28 PCA</span>
                <span class="flow-arrow">➔</span>
                <span class="flow-node">XGBOOST</span>
                <span class="flow-arrow">➔</span>
                <span class="flow-node">SHAP</span>
                <span class="flow-arrow">➔</span>
                <span class="flow-node">DECISION</span>
            </div>
        </div>
    </div>
    """

    hero_right_html = f"""
    <div class="hero-right-column slow-motion-cinematic">
        <div class="hero-3d-stage">
            <!-- Background Signal Vector Paths (Card -> Node -> AEGIS Core) -->
            <svg class="card-signal-svg" viewBox="0 0 400 350" preserveAspectRatio="none">
                <path d="M 50 50 Q 200 100 200 175" class="signal-line" />
                <path d="M 350 50 Q 200 100 200 175" class="signal-line" />
                <path d="M 30 175 Q 120 175 200 175" class="signal-line" />
                <path d="M 370 175 Q 280 175 200 175" class="signal-line" />
                <path d="M 80 300 Q 140 240 200 175" class="signal-line" />
                <path d="M 320 300 Q 260 240 200 175" class="signal-line" />
                <circle cx="200" cy="175" r="4" class="signal-pulse-dot" />
            </svg>

            <div class="ai-radar-core">
                <div class="radar-ring radar-ring-1"></div>
                <div class="radar-ring radar-ring-2"></div>
                <div class="radar-ring radar-ring-3"></div>
                <div class="radar-laser-beam"></div>
                <div class="ai-core-orb-glowing">🛡️</div>
            </div>

            <!-- 6 Orbiting 3D Glass Payment Cards -->
            <div class="card-3d-float card-pos-visa">
                <div class="card-header-flex">
                    <div class="card-chip-gold"></div>
                    <div class="card-brand-title" style="color: #FFD700;">VISA GOLD</div>
                </div>
                <div class="card-num-code">•••• 4892</div>
            </div>

            <div class="card-3d-float card-pos-mastercard">
                <div class="card-header-flex">
                    <div class="card-chip-gold"></div>
                    <div class="card-brand-title" style="color: #EF4444;">MASTER</div>
                </div>
                <div class="card-num-code">•••• 9104</div>
            </div>

            <div class="card-3d-float card-pos-amex">
                <div class="card-header-flex">
                    <div class="card-chip-gold"></div>
                    <div class="card-brand-title" style="color: #00F0FF;">AMEX</div>
                </div>
                <div class="card-num-code">•••• 1120</div>
            </div>

            <div class="card-3d-float card-pos-applepay">
                <div class="card-header-flex">
                    <div class="card-chip-gold"></div>
                    <div class="card-brand-title" style="color: #FFFFFF;"> PAY</div>
                </div>
                <div class="card-num-code">•••• 8831</div>
            </div>

            <div class="card-3d-float card-pos-crypto">
                <div class="card-header-flex">
                    <div class="card-chip-gold"></div>
                    <div class="card-brand-title" style="color: #8B5CF6;">USDT/BTC</div>
                </div>
                <div class="card-num-code">0x9F4A...</div>
            </div>

            <div class="card-3d-float card-pos-swift">
                <div class="card-header-flex">
                    <div class="card-chip-gold"></div>
                    <div class="card-brand-title" style="color: #10B981;">SWIFT WIRE</div>
                </div>
                <div class="card-num-code">WIRE #9910</div>
            </div>
        </div>

        <!-- Model Intelligence Console Panel -->
        <div class="hero-mini-hud">
            <div class="hud-header">
                <div class="hud-title">⚡ MODEL INTELLIGENCE CONSOLE</div>
                <div class="hud-badge">HOLDOUT 80/20 EVAL</div>
            </div>
            <div class="hud-metrics-grid">
                <div class="hud-metric-item">
                    <span class="hud-label">TEST ACCURACY</span>
                    <span class="hud-val" style="color: #00F0FF;">{m_stats['test_accuracy']:.2f}%</span>
                </div>
                <div class="hud-metric-item">
                    <span class="hud-label">TEST RECALL</span>
                    <span class="hud-val" style="color: #10B981;">{m_stats['test_recall']:.2f}%</span>
                </div>
                <div class="hud-metric-item">
                    <span class="hud-label">TEST PRECISION</span>
                    <span class="hud-val" style="color: #F59E0B;">{m_stats['test_precision']:.2f}%</span>
                </div>
                <div class="hud-metric-item">
                    <span class="hud-label">ROC-AUC</span>
                    <span class="hud-val" style="color: #8B5CF6;">{m_stats['test_auc']:.4f}</span>
                </div>
            </div>
        </div>
    </div>
    """

    with st.container():
        c1, c2 = st.columns([1.15, 0.85])
        with c1:
            safe_html(hero_left_html)
            b1, b2 = st.columns([1, 1])
            with b1:
                if st.button("🚀 Start Live Monitoring", key="hero_btn_mon", type="primary", use_container_width=True):
                    st.session_state.current_page = "Dashboard"
                    st.rerun()
            with b2:
                if st.button("📡 Live SOC Radar", key="hero_btn_radar", type="secondary", use_container_width=True):
                    st.session_state.current_page = "Dashboard"
                    st.rerun()
        with c2:
            safe_html(hero_right_html)

    # Lower Hero: AI Threat Intelligence Grid Visualization Panel
    threat_grid_html = """
    <div class="aegis-threat-grid-container">
        <div class="threat-grid-header">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span class="threat-grid-pulse"></span>
                <span class="threat-grid-title">⚡ AI THREAT INTELLIGENCE GRID — XGBOOST INFERENCE PIPELINE</span>
            </div>
            <span class="threat-grid-tag">SUB-MILLISECOND INFERENCE ENGINE</span>
        </div>

        <div class="threat-pipeline-flow">
            <div class="threat-node">
                <div class="node-icon">💳</div>
                <div class="node-body">
                    <div class="node-step">STAGE 01</div>
                    <div class="node-name">RAW TRANSACTION</div>
                    <div class="node-desc">Time + Amount Ingestion</div>
                </div>
            </div>

            <div class="threat-connector">
                <div class="connector-line"></div>
                <div class="connector-packet"></div>
            </div>

            <div class="threat-node">
                <div class="node-icon">⚙️</div>
                <div class="node-body">
                    <div class="node-step">STAGE 02</div>
                    <div class="node-name">FEATURE VECTOR</div>
                    <div class="node-desc">V1–V28 PCA Signals</div>
                </div>
            </div>

            <div class="threat-connector">
                <div class="connector-line"></div>
                <div class="connector-packet"></div>
            </div>

            <div class="threat-node node-active-xgboost">
                <div class="node-icon">🤖</div>
                <div class="node-body">
                    <div class="node-step">STAGE 03</div>
                    <div class="node-name">XGBOOST CLASSIFIER</div>
                    <div class="node-desc">Gradient-Boosted Trees</div>
                </div>
            </div>

            <div class="threat-connector">
                <div class="connector-line"></div>
                <div class="connector-packet"></div>
            </div>

            <div class="threat-node">
                <div class="node-icon">📊</div>
                <div class="node-body">
                    <div class="node-step">STAGE 04</div>
                    <div class="node-name">SHAP EXPLANATION</div>
                    <div class="node-desc">Feature Impact Matrix</div>
                </div>
            </div>

            <div class="threat-connector">
                <div class="connector-line"></div>
                <div class="connector-packet"></div>
            </div>

            <div class="threat-node node-decision">
                <div class="node-icon">🛡️</div>
                <div class="node-body">
                    <div class="node-step">STAGE 05</div>
                    <div class="node-name">POLICY DECISION</div>
                    <div class="node-desc">Clear / Block Action</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Premium Entry Statement (Replaces Scroll Down Indicator) -->
    <div class="aegis-mission-entry-container">
        <blockquote class="aegis-mission-quote">
            "Every transaction leaves a signal. AEGIS turns that signal into a decision."
        </blockquote>
        <div class="aegis-mission-sublabel">
            AI-DRIVEN FRAUD INTELLIGENCE • XGBOOST • EXPLAINABLE RISK SCORING
        </div>
    </div>
    """
    safe_html(threat_grid_html)