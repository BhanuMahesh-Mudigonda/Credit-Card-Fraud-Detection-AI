import streamlit as st

# 1. Page Configuration (Wide Layout, Hides sidebar by default)
st.set_page_config(
    page_title="AEGIS AI | Enterprise Fraud Intelligence Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject Custom Cyber SOC CSS
from utils.theme import load_css
load_css()

# 3. Render 8-Layer Animated Ambient Cyber Background
from components.background import render_ambient_background
render_ambient_background()

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

# 5. Render Sticky Glass Top Navigation Bar
render_top_navbar()

# 6. Route to Active Page View (Instantaneous Rendering)
current_page = st.session_state.get("current_page", "Home")

if current_page == "Home":
    render_home_view()
elif current_page == "Dataset":
    render_dataset_view()
elif current_page == "Prediction":
    render_prediction_view()
elif current_page == "Performance":
    render_performance_view()
elif current_page == "Explain AI":
    render_explain_ai_view()
elif current_page == "Dashboard":
    render_dashboard_view()
elif current_page == "Reports":
    render_reports_view()
elif current_page == "About":
    render_about_view()
else:
    render_home_view()