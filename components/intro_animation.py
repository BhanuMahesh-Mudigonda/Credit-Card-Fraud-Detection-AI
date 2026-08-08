import streamlit as st
from utils.theme import safe_html

def render_intro_animation(force_play=False):
    if not force_play and st.session_state.get("intro_played", False):
        return

    st.session_state.intro_played = True

    reveal_html = """
    <div id="aegis-fast-activation">
        <div id="activation-scan-line"></div>
        <div id="activation-badge">
            <span class="act-pulse"></span>
            <span>🛡️ AEGIS AI SOC ACTIVATED | SYSTEM ONLINE</span>
        </div>
    </div>

    <style>
    #aegis-fast-activation {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 99999; pointer-events: none; overflow: hidden;
        animation: fastActivationFade 0.75s ease-out forwards;
    }

    #activation-scan-line {
        position: absolute; top: 0; left: 0; width: 100%; height: 4px;
        background: linear-gradient(90deg, transparent, #00F0FF, #8B5CF6, #FFD700, transparent);
        box-shadow: 0 0 35px #00F0FF, 0 0 70px #8B5CF6;
        animation: scanLineSweep 0.65s ease-in-out forwards;
    }

    #activation-badge {
        position: fixed; top: 80px; right: 35px; z-index: 100000;
        display: flex; align-items: center; gap: 10px;
        padding: 9px 20px; border-radius: 30px;
        background: rgba(4, 6, 18, 0.95); border: 1.5px solid #00F0FF;
        color: #00F0FF; font-family: 'Space Grotesk', sans-serif;
        font-weight: 800; font-size: 0.84rem; letter-spacing: 1px;
        box-shadow: 0 0 35px rgba(0, 240, 255, 0.5);
        animation: badgePulsePop 0.9s ease-out forwards;
    }

    .act-pulse {
        width: 9px; height: 9px; background: #10B981; border-radius: 50%;
        box-shadow: 0 0 14px #10B981; animation: actPulseAnim 1.2s infinite;
    }

    @keyframes scanLineSweep {
        0% { top: 0; opacity: 1; }
        100% { top: 100vh; opacity: 0; }
    }

    @keyframes badgePulsePop {
        0% { opacity: 0; transform: translateY(-15px) scale(0.85); }
        40% { opacity: 1; transform: translateY(0) scale(1.06); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    @keyframes actPulseAnim {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(1.5); }
    }

    @keyframes fastActivationFade {
        0% { opacity: 1; }
        75% { opacity: 1; }
        100% { opacity: 0; visibility: hidden; }
    }
    </style>
    """
    safe_html(reveal_html)

