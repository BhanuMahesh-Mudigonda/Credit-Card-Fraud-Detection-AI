import streamlit as st
from utils.theme import safe_html

def render_ambient_background():
    bg_html = """
    <!-- 8-Layer Animated Ambient Cyber Background -->
    <div id="aegis-8layer-bg">
        <!-- Layer 1: Moving Stars Canvas -->
        <canvas id="bg-stars-canvas"></canvas>

        <!-- Layer 2: Aurora Gradients -->
        <div class="aurora-bg-layer"></div>

        <!-- Layer 3: Cyber Grid Pattern -->
        <div class="cyber-grid-layer"></div>

        <!-- Layer 4: Neural Network Connection Canvas -->
        <canvas id="bg-neural-canvas"></canvas>

        <!-- Layer 5: World Map Topology Vector Overlay -->
        <div class="world-map-bg-layer"></div>

        <!-- Layer 6: Ambient Moving Particles Canvas -->
        <canvas id="bg-particles-canvas"></canvas>

        <!-- Layer 7: Volumetric Light Rays -->
        <div class="light-rays-layer"></div>

        <!-- Layer 8: Interactive Mouse Glow Light Follower -->
        <div id="mouse-glow-follower"></div>
    </div>

    <style>
    #aegis-8layer-bg {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1; pointer-events: none; overflow: hidden; background: #050816;
    }

    /* Layer 1 & 4 & 6 Canvases */
    #bg-stars-canvas, #bg-neural-canvas, #bg-particles-canvas {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    }

    /* Layer 2: Aurora Gradients */
    .aurora-bg-layer {
        position: absolute; top: -30%; left: -20%; width: 140%; height: 140%;
        background: 
            radial-gradient(ellipse 60% 40% at 20% 20%, rgba(0, 212, 255, 0.18), transparent 70%),
            radial-gradient(ellipse 50% 50% at 80% 70%, rgba(124, 58, 237, 0.18), transparent 70%),
            radial-gradient(ellipse 40% 60% at 50% 40%, rgba(0, 212, 255, 0.1), transparent 60%);
        filter: blur(50px); animation: ambientAurora 18s ease-in-out infinite alternate;
    }
    @keyframes ambientAurora {
        0% { transform: scale(1) translate(0, 0) rotate(0deg); }
        50% { transform: scale(1.1) translate(-30px, 20px) rotate(2deg); }
        100% { transform: scale(1.05) translate(30px, -20px) rotate(-2deg); }
    }

    /* Layer 3: Cyber Grid Pattern */
    .cyber-grid-layer {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-size: 45px 45px;
        background-image: 
            linear-gradient(to right, rgba(0, 212, 255, 0.03) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(0, 212, 255, 0.03) 1px, transparent 1px);
    }

    /* Layer 5: World Map Overlay */
    .world-map-bg-layer {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at center, rgba(8, 27, 51, 0.4), transparent 80%);
        opacity: 0.6;
    }

    /* Layer 7: Volumetric Light Rays */
    .light-rays-layer {
        position: absolute; top: -50%; left: 30%; width: 40%; height: 200%;
        background: linear-gradient(180deg, rgba(0, 212, 255, 0.05), transparent 80%);
        transform: rotate(-25deg); animation: lightRayMove 12s ease-in-out infinite alternate;
    }
    @keyframes lightRayMove {
        0% { opacity: 0.3; transform: rotate(-25deg) translateX(-40px); }
        100% { opacity: 0.8; transform: rotate(-25deg) translateX(40px); }
    }

    /* Layer 8: Mouse Glow Follower */
    #mouse-glow-follower {
        position: fixed; width: 350px; height: 350px; border-radius: 50%;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.15), transparent 70%);
        pointer-events: none; transform: translate(-50%, -50%);
        transition: left 0.15s ease-out, top 0.15s ease-out; z-index: 0;
    }
    </style>

    <script>
    (function Init8LayerBackground() {
        if (window.__aegisBgInitialized) return;
        window.__aegisBgInitialized = true;

        // Mouse glow tracker
        const mouseGlow = document.getElementById('mouse-glow-follower');
        window.addEventListener('mousemove', (e) => {
            if (mouseGlow) {
                mouseGlow.style.left = e.clientX + 'px';
                mouseGlow.style.top = e.clientY + 'px';
            }
        });

        // Layer 1: Moving Stars
        const starsCanvas = document.getElementById('bg-stars-canvas');
        if (starsCanvas) {
            const ctx = starsCanvas.getContext('2d');
            starsCanvas.width = window.innerWidth;
            starsCanvas.height = window.innerHeight;
            const stars = [];
            for (let i = 0; i < 90; i++) {
                stars.push({
                    x: Math.random() * starsCanvas.width,
                    y: Math.random() * starsCanvas.height,
                    r: Math.random() * 1.5 + 0.5,
                    vx: (Math.random() - 0.5) * 0.4,
                    vy: (Math.random() - 0.5) * 0.4,
                    alpha: Math.random() * 0.7 + 0.3
                });
            }
            function animStars() {
                ctx.clearRect(0, 0, starsCanvas.width, starsCanvas.height);
                stars.forEach(s => {
                    s.x += s.vx; s.y += s.vy;
                    if (s.x < 0) s.x = starsCanvas.width;
                    if (s.x > starsCanvas.width) s.x = 0;
                    if (s.y < 0) s.y = starsCanvas.height;
                    if (s.y > starsCanvas.height) s.y = 0;
                    ctx.beginPath();
                    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(255, 255, 255, ${s.alpha})`;
                    ctx.fill();
                });
                requestAnimationFrame(animStars);
            }
            animStars();
        }

        // Layer 4: Neural Network Connection Lines
        const neuralCanvas = document.getElementById('bg-neural-canvas');
        if (neuralCanvas) {
            const nctx = neuralCanvas.getContext('2d');
            neuralCanvas.width = window.innerWidth;
            neuralCanvas.height = window.innerHeight;
            const nodes = [];
            for (let i = 0; i < 35; i++) {
                nodes.push({
                    x: Math.random() * neuralCanvas.width,
                    y: Math.random() * neuralCanvas.height,
                    vx: (Math.random() - 0.5) * 0.6,
                    vy: (Math.random() - 0.5) * 0.6
                });
            }
            function animNeural() {
                nctx.clearRect(0, 0, neuralCanvas.width, neuralCanvas.height);
                for (let i = 0; i < nodes.length; i++) {
                    nodes[i].x += nodes[i].vx; nodes[i].y += nodes[i].vy;
                    if (nodes[i].x < 0 || nodes[i].x > neuralCanvas.width) nodes[i].vx *= -1;
                    if (nodes[i].y < 0 || nodes[i].y > neuralCanvas.height) nodes[i].vy *= -1;

                    for (let j = i + 1; j < nodes.length; j++) {
                        const dx = nodes[i].x - nodes[j].x;
                        const dy = nodes[i].y - nodes[j].y;
                        const dist = Math.sqrt(dx * dx + dy * dy);
                        if (dist < 140) {
                            nctx.beginPath();
                            nctx.moveTo(nodes[i].x, nodes[i].y);
                            nctx.lineTo(nodes[j].x, nodes[j].y);
                            nctx.strokeStyle = `rgba(0, 212, 255, ${0.12 * (1 - dist / 140)})`;
                            nctx.lineWidth = 1;
                            nctx.stroke();
                        }
                    }
                }
                requestAnimationFrame(animNeural);
            }
            animNeural();
        }
    })();
    </script>
    """
    safe_html(bg_html)
