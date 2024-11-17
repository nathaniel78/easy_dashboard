# src/fragments/footer.py
import streamlit as st
from src.core.param import (
    FOOTER_COPYRIGTH
)

def render_footer():
    st.markdown(
        f"""
        <footer>
            {FOOTER_COPYRIGTH}
        </footer>
        """,
        unsafe_allow_html=True
    )
