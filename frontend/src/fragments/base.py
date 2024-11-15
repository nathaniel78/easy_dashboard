# src/fragments/base.py
import streamlit as st
from . import header, sidebar, footer
from pathlib import Path

st.set_page_config(
        layout="wide"
    )

def render_base(content_func):
    """Função que renderiza a estrutura base da aplicação."""
    
    # Function to load css
    def load_css(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
    # Load css
    css_path = Path("src/static/css/style.css")
    load_css(css_path)
    
    # Render header
    header.render_header()

    col1, col2 = st.columns([1, 4])

    # Sidebar
    with col1:
        sidebar.render_sidebar() 

    # Content area
    with col2:
        content_func()

    # Render footer
    footer.render_footer()
