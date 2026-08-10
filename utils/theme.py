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
    """Guarantees target page opens at absolute top (0,0) matching Image 2 without jerk."""
    if not force:
        return

    scroll_js = """
    <script>
    (function resetToTopNow() {
        try {
            var doc = (window.parent && window.parent.document) ? window.parent.document : document;
            var win = window.parent || window;
            
            if ('scrollRestoration' in win.history) {
                win.history.scrollRestoration = 'manual';
            }
            if ('scrollRestoration' in window.history) {
                window.history.scrollRestoration = 'manual';
            }

            function setTop() {
                var appView = doc.querySelector('[data-testid="stAppViewContainer"]') || 
                               doc.querySelector('section.main') || 
                               doc.documentElement || 
                               doc.body;
                if (appView) {
                    appView.scrollTop = 0;
                    appView.scrollLeft = 0;
                    if (typeof appView.scrollTo === 'function') {
                        appView.scrollTo({top: 0, left: 0, behavior: 'instant'});
                    }
                }
                if (typeof win.scrollTo === 'function') {
                    win.scrollTo({top: 0, left: 0, behavior: 'instant'});
                }
            }

            setTop();
            setTimeout(setTop, 10);
            setTimeout(setTop, 50);
            setTimeout(setTop, 100);
        } catch (e) {
            console.log("AEGIS Scroll Reset:", e);
        }
    })();
    </script>
    """
    safe_html(scroll_js)