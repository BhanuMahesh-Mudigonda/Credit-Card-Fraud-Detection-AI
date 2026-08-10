import streamlit as st

# 1. Page Configuration (Wide Layout, Hides sidebar by default)
st.set_page_config(
    page_title="AEGIS AI | Enterprise Fraud Intelligence Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject Custom Cyber SOC CSS & Scroll Reset
from utils.theme import load_css, reset_scroll_to_top
load_css()
reset_scroll_to_top()

# 3. Render 8-Layer Animated Ambient Cyber Background & Fast Activation
from components.background import render_ambient_background
from components.intro_animation import render_intro_animation
from components.floating_assistant import render_floating_assistant

render_ambient_background()
render_intro_animation()
render_floating_assistant()

# 4. Import Navigation Component & Page Views
from components.navbar import render_top_navbar
from views.home_view import render_home_view
from views.dataset_view import render_dataset_view
from views.prediction_view import render_prediction_view
from views.performance_view import render_performance_view
from views.explain_ai_view import render_explain_ai_view
from views.dashboard_view import render_dashboard_view
from views.reports_view import render_reports_view
from views.about_view import render_about_view
from components.copilot import render_copilot_quick_button
from components.footer import footer

# 5. Native Streamlit Multipage Navigation Definition
home_page = st.Page(render_home_view, title="Home", icon="🏠", default=True)
dataset_page = st.Page(render_dataset_view, title="Dataset", icon="📊")
prediction_page = st.Page(render_prediction_view, title="Prediction", icon="🤖")
performance_page = st.Page(render_performance_view, title="Performance", icon="📈")
explain_page = st.Page(render_explain_ai_view, title="Explain AI", icon="🧠")
dashboard_page = st.Page(render_dashboard_view, title="Dashboard", icon="📡")
reports_page = st.Page(render_reports_view, title="Reports", icon="📄")
about_page = st.Page(render_about_view, title="About", icon="ℹ️")

pages_map = {
    "Home": home_page,
    "Dataset": dataset_page,
    "Prediction": prediction_page,
    "Performance": performance_page,
    "Explain AI": explain_page,
    "Dashboard": dashboard_page,
    "Reports": reports_page,
    "About": about_page
}

# 6. Render Sticky Glass Top Navigation Bar
render_top_navbar()

current_page = st.session_state.get("current_page", "Home")
last_page = st.session_state.get("_last_rendered_page", None)
page_changed = (current_page != last_page)

if page_changed:
    st.session_state["_last_rendered_page"] = current_page

# Native Page Execution via Streamlit Navigation Engine
active_page = pages_map.get(current_page, home_page)
pg = st.navigation([active_page], position="hidden")
pg.run()

# Instantaneous Scroll Reset on Navigation
if page_changed:
    reset_scroll_to_top(force=True)

# 7. Render Floating Copilot Quick Trigger Button & Footer
render_copilot_quick_button()
footer()