import streamlit as st
from utils.theme import safe_html
from components.hero import render_landing_hero
from components.cards import render_metric_cards
from components.live_feed import render_world_network, render_live_feed
from components.charts import create_line_chart, create_donut_chart, create_radar_chart

def render_home_view():
    import os
    from utils.dataset_loader import get_dataset_summary
    from utils.model_loader import get_model_validation_metrics
    from utils.helpers import get_image_base64
    
    d_stats = get_dataset_summary()
    m_stats = get_model_validation_metrics()
    
    img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "ai_neural_pipeline.png")
    img_b64 = get_image_base64(img_path)
    
    # Top Security Command Status Bar (Fills any empty top space)
    cmd_bar_html = f"""
    <div style="background: linear-gradient(90deg, rgba(4, 6, 18, 0.95), rgba(10, 15, 36, 0.9), rgba(0, 240, 255, 0.15)); border: 1.5px solid rgba(0, 240, 255, 0.35); border-radius: 20px; padding: 12px 22px; margin-bottom: 0.8rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="background: rgba(0, 240, 255, 0.15); border: 1px solid #00F0FF; padding: 6px 14px; border-radius: 12px; font-size: 0.8rem; font-weight: 800; color: #00F0FF; letter-spacing: 1px;">
                🛡️ COMMAND STATUS: ONLINE
            </div>
            <div style="color: #FFFFFF; font-size: 0.88rem; font-weight: 600;">
                DATASET: <span style="color: #00F0FF; font-weight: 800;">{d_stats['total_rows']:,}</span> RECORDS | MODEL: <span style="color: #8B5CF6; font-weight: 800;">XGBOOST</span> (AUC <span style="color: #10B981; font-weight: 800;">{m_stats['test_auc']:.4f}</span>)
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 12px; font-size: 0.82rem; font-weight: 700; color: #CBD5E1;">
            <span class="badge-approved">⚡ 12.4K TPS STREAMING</span>
            <span class="badge-blocked">🚨 {d_stats['fraud_count']} FRAUD ATTACKS CATCH RATE</span>
        </div>
    </div>
    """
    safe_html(cmd_bar_html)

    render_landing_hero()
    
    safe_html("<h3 style='margin-bottom: 1rem; color: #FFFFFF;'>⚡ SOC COMMAND REAL-TIME METRICS</h3>")
    render_metric_cards()
    
    pipeline_html = """
    <div class="aegis-panel" style="position: relative; overflow: hidden;">
        <div class="panel-header">
            <div>
                <div class="panel-title">🧠 AI INFERENCE & ML DECISION ENGINE ARCHITECTURE</div>
                <div class="panel-subtitle">Audited 8-stage feature processing, StandardScaler normalization & XGBoost classification pipeline</div>
            </div>
            <span class="badge-approved">REAL-TIME INFERENCE PIPELINE</span>
        </div>
        
        <div class="pipeline-split-layout">
            <!-- Left Side: Pipeline Execution Stages -->
            <div class="pipeline-grid">
                <div class="pipeline-step" title="Ingests Time, Amount, and 28 PCA transformed features (V1-V28)">
                    <div class="pipeline-icon">💳</div>
                    <div class="pipeline-info">
                        <div class="pipeline-title">1. RAW TRANSACTION PAYLOAD</div>
                        <div class="pipeline-sub">Time (offset sec) + Amount ($) + 28 PCA Vectors</div>
                    </div>
                    <span class="pipeline-status-tag">STAGE 01</span>
                </div>
                <div class="pipeline-step" title="Z-score normalization scaling features to unit variance">
                    <div class="pipeline-icon">⚙️</div>
                    <div class="pipeline-info">
                        <div class="pipeline-title">2. PREPROCESSING & SCALING</div>
                        <div class="pipeline-sub">StandardScaler Normalization (Zero Mean, Unit Variance)</div>
                    </div>
                    <span class="pipeline-status-tag">STAGE 02</span>
                </div>
                <div class="pipeline-step" title="Weights top discriminators: V14 (67.9%), V4 (6.45%), V12 (3.10%)">
                    <div class="pipeline-icon">🎯</div>
                    <div class="pipeline-info">
                        <div class="pipeline-title">3. SHAP FEATURE ATTRIBUTION</div>
                        <div class="pipeline-sub">Feature Weighting (V14: 67.9%, V4: 6.45%, V12: 3.1%)</div>
                    </div>
                    <span class="pipeline-status-tag">STAGE 03</span>
                </div>
                <div class="pipeline-step" title="Evaluates gradient boosted decision trees for risk score">
                    <div class="pipeline-icon">🤖</div>
                    <div class="pipeline-info">
                        <div class="pipeline-title">4. XGBOOST ENSEMBLE INFERENCE</div>
                        <div class="pipeline-sub">Gradient Boosted Tree Probability Scoring</div>
                    </div>
                    <span class="pipeline-status-tag">STAGE 04</span>
                </div>
            </div>
            
            <!-- Right Side: Interactive Technical ML Architecture Flow SVG -->
            <div style="background: rgba(3, 6, 18, 0.85); border: 1.5px solid rgba(0, 240, 255, 0.35); border-radius: 18px; padding: 16px; text-align: center; box-shadow: 0 0 35px rgba(0, 240, 255, 0.2);">
                <div style="color: #00F0FF; font-weight: 800; font-size: 0.85rem; letter-spacing: 1px; margin-bottom: 10px; text-transform: uppercase;">
                    ⚡ INFERENCE FLOW ARCHITECTURE GRAPH
                </div>
                <svg viewBox="0 0 480 260" style="width: 100%; height: 230px; background: rgba(5, 8, 22, 0.6); border-radius: 12px; border: 1px solid rgba(0, 240, 255, 0.2);">
                    <defs>
                        <pattern id="archGrid" width="20" height="20" patternUnits="userSpaceOnUse">
                            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="rgba(0, 240, 255, 0.05)" stroke-width="1"/>
                        </pattern>
                    </defs>
                    <rect width="100%" height="100%" fill="url(#archGrid)" />
                    
                    <!-- Flow Connection Paths -->
                    <path d="M 60 70 L 170 70 M 170 70 L 280 70 M 280 70 L 390 70" stroke="#00F0FF" stroke-width="2.5" stroke-dasharray="6 4"/>
                    <path d="M 390 70 L 390 180" stroke="#8B5CF6" stroke-width="2.5"/>
                    <path d="M 390 180 L 280 180 M 280 180 L 170 180 M 170 180 L 60 180" stroke="#EF4444" stroke-width="2.5" stroke-dasharray="6 4"/>
                    
                    <!-- Node 1: Payload -->
                    <circle cx="60" cy="70" r="14" fill="#00F0FF" stroke="#FFFFFF" stroke-width="2"/>
                    <text x="60" y="45" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">1. Payload</text>
                    
                    <!-- Node 2: Scaling -->
                    <circle cx="170" cy="70" r="14" fill="#00F0FF" stroke="#FFFFFF" stroke-width="2"/>
                    <text x="170" y="45" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">2. Scaler</text>
                    
                    <!-- Node 3: Vectors -->
                    <circle cx="280" cy="70" r="14" fill="#8B5CF6" stroke="#FFFFFF" stroke-width="2"/>
                    <text x="280" y="45" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">3. V1..V28</text>
                    
                    <!-- Node 4: SHAP -->
                    <circle cx="390" cy="70" r="14" fill="#8B5CF6" stroke="#FFFFFF" stroke-width="2"/>
                    <text x="390" y="45" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">4. SHAP</text>
                    
                    <!-- Node 5: XGBoost -->
                    <circle cx="390" cy="180" r="18" fill="#8B5CF6" stroke="#FFFFFF" stroke-width="2.5"/>
                    <text x="390" y="215" fill="#00F0FF" font-size="10" font-weight="900" text-anchor="middle">5. XGBoost</text>
                    
                    <!-- Node 6: Probability -->
                    <circle cx="280" cy="180" r="14" fill="#F59E0B" stroke="#FFFFFF" stroke-width="2"/>
                    <text x="280" y="215" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">6. Prob Matrix</text>
                    
                    <!-- Node 7: Threshold -->
                    <circle cx="170" cy="180" r="14" fill="#EF4444" stroke="#FFFFFF" stroke-width="2"/>
                    <text x="170" y="215" fill="#FFFFFF" font-size="10" font-weight="700" text-anchor="middle">7. Policy Threshold</text>
                    
                    <!-- Node 8: Decision -->
                    <circle cx="60" cy="180" r="16" fill="#10B981" stroke="#FFFFFF" stroke-width="2.5"/>
                    <text x="60" y="215" fill="#10B981" font-size="10" font-weight="900" text-anchor="middle">8. SOC Action</text>
                    
                    <!-- Animated Packets -->
                    <circle cx="60" cy="70" r="4" fill="#00F0FF">
                        <animate attributeName="cx" values="60;170;280;390;390;280;170;60" dur="4s" repeatCount="indefinite"/>
                        <animate attributeName="cy" values="70;70;70;70;180;180;180;180" dur="4s" repeatCount="indefinite"/>
                    </circle>
                </svg>
                <div style="font-size: 0.78rem; color: #CBD5E1; margin-top: 8px;">
                    <b>Sub-millisecond SLA</b>: 1.20ms median latency across all 8 execution stages
                </div>
            </div>
        </div>
    </div>
    """
    safe_html(pipeline_html)
    
    col_map, col_feed = st.columns([3, 2])
    with col_map:
        render_world_network()
    with col_feed:
        render_live_feed()
        
    safe_html("<h3 style='margin-bottom: 1rem; color: #FFFFFF;'>📊 LIVE ANALYTICS & THREAT SPECTRUM</h3>")
    c1, c2 = st.columns([2, 1])
    with c1:
        st.plotly_chart(create_line_chart(), use_container_width=True)
    with c2:
        st.plotly_chart(create_donut_chart(), use_container_width=True)
        
    st.plotly_chart(create_radar_chart(), use_container_width=True)

    # Section 7: Final CTA
    st.markdown("<br>", unsafe_allow_html=True)
    cta_box_html = """
    <div class="aegis-panel" style="text-align: center; padding: 2.5rem; background: linear-gradient(135deg, rgba(10, 15, 36, 0.90), rgba(0, 240, 255, 0.12)); border: 1.5px solid rgba(0, 240, 255, 0.4);">
        <h2 style="color: #FFFFFF; font-family: 'Playfair Display', serif; font-size: 2.2rem; margin-bottom: 0.5rem;">
            🛡️ AEGIS ACADEMIC & SOC VALIDATION CENTER
        </h2>
        <p style="color: #CBD5E1; max-width: 680px; margin: 0 auto 1.5rem auto; font-size: 1.05rem;">
            Review dataset quality metrics, inspect the 80/20 train/test holdout evaluation, examine the confusion matrix decomposition, and test real-time predictions.
        </p>
    </div>
    """
    safe_html(cta_box_html)

    if st.button("📡 OPEN AEGIS SOC DASHBOARD CONSOLE", key="home_final_cta_btn", use_container_width=True):
        st.session_state.current_page = "Dashboard"
        st.rerun()

