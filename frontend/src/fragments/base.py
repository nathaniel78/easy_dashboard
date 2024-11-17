# src/fragments/base.py
import streamlit as st
from . import header, sidebar, footer
from pathlib import Path
import json

#------ Config set streamlit ---------#
st.set_page_config(
    page_icon=":chart:",
    layout="wide"
)

#------ Load settings ---------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    with open(settings_path, "r") as file:
        settings = json.load(file)
    return settings

#------ Aviso de manutenção ---------#
def maintenance():
    st.markdown(
            """
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; text-align: center;">
                <h1 style="font-size: 3rem; color: #FF4B4B;">🚧 Página em Manutenção 🚧</h1>
                <p style="font-size: 1.2rem; color: #666;">Estamos trabalhando para melhorar sua experiência.</p>
                <p style="font-size: 1rem; color: #999;">Por favor, volte mais tarde.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

#------ Base ---------#
def render_base(content_func):
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    theme = settings["config_screen"] 
    is_maintenance = settings["config_maintenance"]
    page_admin = st.session_state.get('page')
    
    #---------- Carregar o CSS baseado no tema --------------#
    def load_css(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    if theme == "light":
        css_path = Path("src/static/css/style_light.css")
    else:
        css_path = Path("src/static/css/style_dark.css")
    
    load_css(css_path)
    
    #---------- Renderizar o cabeçalho ------------#
    header.render_header()

    col1, col2 = st.columns([1, 5])

    #--------- Render sidebar ------------#
    with col1:
        sidebar.render_sidebar() 

    #---------- Renderizar conteúdo -----------#
    with col2:
        if page_admin == 'admin':
            content_func()
            
        elif is_maintenance is True:
            maintenance()
            
        else:
            content_func()

    #--------- Renderizar o rodapé ------------#
    footer.render_footer()
