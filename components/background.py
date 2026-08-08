import streamlit as st
from utils.theme import safe_html

def render_ambient_background():
    js_injector = """
    <script>
    (function InjectAegisBackground() {
        const doc = window.parent.document || document;
        
        if (!doc.getElementById('aegis-8layer-bg')) {
            const bgContainer = doc.createElement('div');
            bgContainer.id = 'aegis-8layer-bg';
            bgContainer.style.cssText = 'position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1; pointer-events:none; overflow:hidden; background:#040612;';
            bgContainer.innerHTML = '<canvas id="bg-stars-canvas" style="position:absolute;top:0;left:0;width:100%;height:100%;"></canvas><div class="aurora-bg-layer"></div><div class="cyber-grid-layer"></div><canvas id="bg-neural-canvas" style="position:absolute;top:0;left:0;width:100%;height:100%;"></canvas><div class="world-map-bg-layer"></div><canvas id="bg-particles-canvas" style="position:absolute;top:0;left:0;width:100%;height:100%;"></canvas><div class="light-rays-layer"></div><div id="mouse-glow-follower"></div>';
            doc.body.insertBefore(bgContainer, doc.body.firstChild);
        }

        const mouseGlow = doc.getElementById('mouse-glow-follower');
        if (mouseGlow && !window.__aegisMouseBound) {
            window.__aegisMouseBound = true;
            doc.addEventListener('mousemove', (e) => {
                mouseGlow.style.left = e.clientX + 'px';
                mouseGlow.style.top = e.clientY + 'px';
            });
        }

        const starsCanvas = doc.getElementById('bg-stars-canvas');
        if (starsCanvas && !window.__aegisStarsInit) {
            window.__aegisStarsInit = true;
            const ctx = starsCanvas.getContext('2d');
            starsCanvas.width = doc.documentElement.clientWidth || window.innerWidth;
            starsCanvas.height = doc.documentElement.clientHeight || window.innerHeight;
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
                    ctx.fillStyle = 'rgba(255, 255, 255, ' + s.alpha + ')';
                    ctx.fill();
                });
                requestAnimationFrame(animStars);
            }
            animStars();
        }

        const neuralCanvas = doc.getElementById('bg-neural-canvas');
        if (neuralCanvas && !window.__aegisNeuralInit) {
            window.__aegisNeuralInit = true;
            const nctx = neuralCanvas.getContext('2d');
            neuralCanvas.width = doc.documentElement.clientWidth || window.innerWidth;
            neuralCanvas.height = doc.documentElement.clientHeight || window.innerHeight;
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
                            nctx.strokeStyle = 'rgba(0, 240, 255, ' + (0.12 * (1 - dist / 140)) + ')';
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
    st.components.v1.html(js_injector, height=0)




