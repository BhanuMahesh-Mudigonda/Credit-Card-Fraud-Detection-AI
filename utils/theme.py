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

def reset_scroll_to_top():
    """Single source of truth: Forces browser and Streamlit containers to scroll position (0, 0) top on page navigation."""
    scroll_js = """
    <div id="aegis-page-top" style="position: absolute; top: 0; left: 0; height: 1px; width: 1px; pointer-events: none;"></div>
    <script>
    (function enforceScrollTop() {
        try {
            var doc = (window.parent && window.parent.document) ? window.parent.document : document;
            var win = window.parent || window;
            
            // Set manual scroll restoration
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
                var topAnchor = doc.getElementById('aegis-page-top');
                if (topAnchor && typeof topAnchor.scrollIntoView === 'function') {
                    topAnchor.scrollIntoView({block: 'start', inline: 'nearest', behavior: 'instant'});
                }
                var elements = [
                    doc.querySelector('section.main'),
                    doc.querySelector('.main'),
                    doc.querySelector('[data-testid="stAppViewContainer"]'),
                    doc.querySelector('[data-testid="stMain"]'),
                    doc.querySelector('.block-container'),
                    doc.querySelector('.stApp'),
                    doc.documentElement,
                    doc.body
                ];
                elements.forEach(function(el) {
                    if (el) {
                        el.scrollTop = 0;
                        if (typeof el.scrollTo === 'function') {
                            el.scrollTo({top: 0, left: 0, behavior: 'instant'});
                        }
                    }
                });
                if (typeof win.scrollTo === 'function') {
                    win.scrollTo({top: 0, left: 0, behavior: 'instant'});
                }
            }

            // Immediate execution on render
            setScrollZero();
            setTimeout(setScrollZero, 10);
            setTimeout(setScrollZero, 50);
            setTimeout(setScrollZero, 150);
        } catch (e) {
            console.log("AEGIS Scroll Reset Notice:", e);
        }
    })();
    </script>
    """
    safe_html(scroll_js)