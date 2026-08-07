import streamlit as st
from utils.theme import safe_html

def render_landing_hero():
    hero_html = """
    <div class="hero-viewport-fullscreen">
        <div class="hero-content-split">
            <!-- Left Hero Title & Action Buttons -->
            <div class="hero-left-column">
                <div class="hero-pill-tag">
                    <span class="pulse-green-dot"></span>
                    <span>ENTERPRISE SOC AI • REAL-TIME PROTECTION</span>
                </div>

                <h1 class="hero-main-title">
                    🛡️ AEGIS AI <br>
                    <span class="gradient-text-hero">NEXT GENERATION</span> <br>
                    FRAUD INTELLIGENCE
                </h1>

                <p class="hero-main-subtitle">
                    Enterprise AI protecting global financial infrastructure in real time using advanced machine learning, sub-millisecond XGBoost threat scoring, and automated SOC mitigation.
                </p>

                <!-- Glass Action Buttons -->
                <div class="hero-action-buttons">
                    <button class="btn-glass-primary" onclick="window.scrollTo({top: 800, behavior: 'smooth'})">
                        🚀 Start Monitoring
                    </button>
                    <button class="btn-glass-secondary" onclick="window.scrollTo({top: 1400, behavior: 'smooth'})">
                        📊 View Dashboard
                    </button>
                    <button class="btn-glass-outline" onclick="alert('AEGIS AI Security Operations Center Live Demo Active')">
                        🎬 Watch Demo
                    </button>
                </div>
            </div>

            <!-- Right 4 Orbiting 3D Glass Credit Cards & AI Core -->
            <div class="hero-right-column">
                <div class="ai-core-orbit-center">
                    <!-- Concentric Radar Scanner Rings -->
                    <div class="orbit-scanner-ring ring-outer-glow"></div>
                    <div class="orbit-scanner-ring ring-middle-glow"></div>
                    <div class="orbit-scanner-ring ring-inner-glow"></div>
                    <div class="orbit-radar-laser"></div>

                    <!-- Central AI Core Orb -->
                    <div class="aegis-core-orb">🛡️</div>

                    <!-- 4 Orbiting 3D Glass Credit Cards -->
                    <div class="orbiting-card-wrapper card-orbit-1">
                        <div class="glass-mini-card">
                            <div class="mini-card-chip"></div>
                            <div class="mini-card-brand">VISA</div>
                            <div class="mini-card-num">•••• 4892</div>
                        </div>
                    </div>
                    <div class="orbiting-card-wrapper card-orbit-2">
                        <div class="glass-mini-card">
                            <div class="mini-card-chip"></div>
                            <div class="mini-card-brand">MASTER</div>
                            <div class="mini-card-num">•••• 9104</div>
                        </div>
                    </div>
                    <div class="orbiting-card-wrapper card-orbit-3">
                        <div class="glass-mini-card">
                            <div class="mini-card-chip"></div>
                            <div class="mini-card-brand">AMEX</div>
                            <div class="mini-card-num">•••• 1120</div>
                        </div>
                    </div>
                    <div class="orbiting-card-wrapper card-orbit-4">
                        <div class="glass-mini-card">
                            <div class="mini-card-chip"></div>
                            <div class="mini-card-brand">CORP</div>
                            <div class="mini-card-num">•••• 8831</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    safe_html(hero_html)