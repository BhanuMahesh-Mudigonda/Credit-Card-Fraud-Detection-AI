import streamlit as st
from utils.theme import safe_html
from components.hero import render_landing_hero
from components.cards import render_metric_cards
from components.live_feed import render_world_network, render_live_feed
from components.charts import create_line_chart, create_donut_chart, create_radar_chart

def render_home_view():
    render_landing_hero()
    
    safe_html("<h3 style='margin-bottom: 1rem; color: #FFFFFF;'>⚡ SOC COMMAND REAL-TIME METRICS</h3>")
    render_metric_cards()
    
    pipeline_html = """
    <div class="aegis-panel">
        <div class="panel-header">
            <div>
                <div class="panel-title">🧠 AI DECISION ENGINE PIPELINE</div>
                <div class="panel-subtitle">Sub-millisecond automated fraud evaluation flow</div>
            </div>
            <span class="badge-approved">ACTIVE 5-STAGE PIPELINE</span>
        </div>
        <div class="pipeline-grid">
            <div class="pipeline-step active">
                <div class="pipeline-icon">💳</div>
                <div class="pipeline-title">1. SCANNING</div>
                <div class="pipeline-sub">Real-time Ingestion</div>
                <div class="pipeline-arrow">➔</div>
            </div>
            <div class="pipeline-step active">
                <div class="pipeline-icon">⚙️</div>
                <div class="pipeline-title">2. EXTRACTION</div>
                <div class="pipeline-sub">28 PCA Features</div>
                <div class="pipeline-arrow">➔</div>
            </div>
            <div class="pipeline-step active">
                <div class="pipeline-icon">🎯</div>
                <div class="pipeline-title">3. RISK ANALYSIS</div>
                <div class="pipeline-sub">XGBoost Scoring</div>
                <div class="pipeline-arrow">➔</div>
            </div>
            <div class="pipeline-step active">
                <div class="pipeline-icon">🤖</div>
                <div class="pipeline-title">4. PREDICTION</div>
                <div class="pipeline-sub">Fraud Probability</div>
                <div class="pipeline-arrow">➔</div>
            </div>
            <div class="pipeline-step active">
                <div class="pipeline-icon">🛡️</div>
                <div class="pipeline-title">5. DECISION</div>
                <div class="pipeline-sub">Auto-Block / Pass</div>
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
