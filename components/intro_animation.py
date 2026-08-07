import streamlit as st
from utils.theme import safe_html

def render_intro_animation(force_play=False):
    if not force_play and st.session_state.get("intro_played", False):
        return

    st.session_state.intro_played = True

    reveal_html = """
    <!-- Instant 0.75s Cinematic Electric Flash Reveal (No Loading Screens) -->
    <div id="aegis-instant-reveal">
        <div id="reveal-flash-bloom"></div>
        <div id="reveal-shield-assembler">
            <div class="reveal-shield-icon">🛡️</div>
            <div class="reveal-brand-title">AEGIS AI</div>
            <div class="reveal-radar-sweep"></div>
        </div>
    </div>

    <style>
    #aegis-instant-reveal {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: 999999; background: #03050F; pointer-events: none;
        display: flex; align-items: center; justify-content: center;
        animation: revealFadeOut 0.75s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }

    #reveal-flash-bloom {
        position: absolute; width: 500px; height: 500px; border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.8), rgba(124, 58, 237, 0.4), transparent 70%);
        animation: electricFlash 0.5s ease-out forwards;
    }

    #reveal-shield-assembler {
        position: relative; z-index: 10; text-align: center;
        animation: shieldZoom 0.65s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }

    .reveal-shield-icon {
        font-size: 90px; filter: drop-shadow(0 0 40px #00D4FF) drop-shadow(0 0 80px #7C3AED);
    }

    .reveal-brand-title {
        font-family: 'Space Grotesk', sans-serif; font-size: 3.5rem; font-weight: 900;
        background: linear-gradient(90deg, #FFFFFF, #00D4FF, #7C3AED);
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent; letter-spacing: 2px;
    }

    .reveal-radar-sweep {
        position: absolute; top: -20px; left: 50%; transform: translateX(-50%);
        width: 280px; height: 280px; border-radius: 50%;
        border: 2px dashed rgba(0, 212, 255, 0.6);
        animation: radarSpin 0.6s linear infinite;
    }

    @keyframes electricFlash {
        0% { transform: scale(0.2); opacity: 0; }
        50% { transform: scale(1.5); opacity: 0.9; }
        100% { transform: scale(2.5); opacity: 0; }
    }

    @keyframes shieldZoom {
        0% { transform: scale(0.4); opacity: 0; }
        60% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1.2); opacity: 0; }
    }

    @keyframes radarSpin {
        from { transform: translateX(-50%) rotate(0deg); }
        to { transform: translateX(-50%) rotate(360deg); }
    }

    @keyframes revealFadeOut {
        0% { opacity: 1; }
        80% { opacity: 1; }
        100% { opacity: 0; visibility: hidden; }
    }
    </style>
    """
    safe_html(reveal_html)
