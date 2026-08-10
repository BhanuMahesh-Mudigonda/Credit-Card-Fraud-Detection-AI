import re
import streamlit as st
from pathlib import Path

def safe_html(html_str):
    # 1. Strip all HTML comments (<!-- ... -->) completely
    clean = re.sub(r'<!--.*?-->', '', html_str, flags=re.DOTALL)
    # 2. Use native st.html to inject raw HTML directly without CommonMark markdown parsing
    st.html(clean)


def get_cached_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            return f.read()
    return ""

def load_css():
    css_content = get_cached_css()
    if css_content:
        st.html(f"<style>\n{css_content}\n</style>")

def reset_scroll_to_top(force=False):
    """Single source of truth: Instantly resets [data-testid="stAppViewContainer"] and document viewport to top (0,0)."""
    if not force:
        return

    scroll_js = """
    <div id="aegis-page-top" style="position: absolute; top: 0; left: 0; height: 1px; width: 1px; pointer-events: none;"></div>
    <script>
    (function enforceScrollTop() {
        try {
            var doc = (window.parent && window.parent.document) ? window.parent.document : document;
            var win = window.parent || window;
            
            // Disable browser automatic scroll restoration
            if ('scrollRestoration' in win.history) {
                win.history.scrollRestoration = 'manual';
            }
            if ('scrollRestoration' in window.history) {
                window.history.scrollRestoration = 'manual';
            }

            if (win.location && win.location.hash) {
                win.history.replaceState(null, "", win.location.pathname);
            }

            function setScrollZero() {
                // Primary Target: Streamlit's actual scrolling container
                var appView = doc.querySelector('[data-testid="stAppViewContainer"]');
                if (appView) {
                    appView.scrollTop = 0;
                    appView.scrollLeft = 0;
                    if (typeof appView.scrollTo === 'function') {
                        appView.scrollTo({top: 0, left: 0, behavior: 'instant'});
                    }
                }

                // Secondary & Viewport Targets (Iterate all without short-circuiting)
                var targets = [
                    doc.querySelector('section.main'),
                    doc.querySelector('.main'),
                    doc.querySelector('[data-testid="stMain"]'),
                    doc.querySelector('.block-container'),
                    doc.documentElement,
                    doc.body
                ];

                targets.forEach(function(el) {
                    if (el) {
                        el.scrollTop = 0;
                        el.scrollLeft = 0;
                        if (typeof el.scrollTo === 'function') {
                            el.scrollTo({top: 0, left: 0, behavior: 'instant'});
                        }
                    }
                });

                if (typeof win.scrollTo === 'function') {
                    win.scrollTo({top: 0, left: 0, behavior: 'instant'});
                }
                if (typeof window.scrollTo === 'function') {
                    window.scrollTo({top: 0, left: 0, behavior: 'instant'});
                }
            }

            // Execute instant scroll reset synchronized with browser paint
            win.requestAnimationFrame(function() {
                setScrollZero();
            });
        } catch (e) {
            console.log("AEGIS Instant Scroll Reset:", e);
        }
    })();
    </script>
    """
    safe_html(scroll_js)