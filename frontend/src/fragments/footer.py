# src/fragments/footer.py
import streamlit as st

def render_footer():
    st.markdown("<footer style='text-align: center;'>© 2024 EasyDashboard</footer>", unsafe_allow_html=True)
