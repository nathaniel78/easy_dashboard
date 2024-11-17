import streamlit as st
from pathlib import Path
from src.core.param import (
    SESSION_TIME
)
import json
import time

#-------- Carregar settings ----------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    
    if settings_path.exists():
        with open(settings_path, "r") as f:
            settings = json.load(f)
        return settings
    else:
        st.error("Arquivo de settings não encontrado.")
        return None

#-------- Salvar settings ---------#
def save_settings(settings):
    settings_path = Path("src/core/settings.json")
    
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)
    st.success("Configurações salvas com sucesso!")
    

#-------- Definir tempo de sessão ---------#
def check_session_timeout():
    session_timeout = SESSION_TIME
    
    if 'last_activity' in st.session_state:
        current_time = time.time()
        time_diff = current_time - st.session_state.last_activity
        
        if time_diff > session_timeout:
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state['page'] = None
            st.warning("Sessão expirada. Por favor, faça login novamente.")
            st.experimental_rerun()

    st.session_state.last_activity = time.time()

#-------- Admin ----------#
def render_admin():
    #------- Valida sessão ---------#
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.warning("Você precisa fazer login para acessar esta página.")
        st.session_state['page'] = 'home' 
        st.experimental_rerun()
    else:
        #-------- Sucesso login ----------#
        check_session_timeout()
        
        st.title("Página Administrativa")
        st.write("Bem-vindo à página de administração.")
        
        #------- Carregar configurações ---------#
        settings = load_settings()
        if settings is None:
            return

        st.subheader("Configurações da aplicação")
        
        #----------- Configurar cor do template ---------#
        template_color = st.selectbox(
            "Configurar cor do template",
            ["light", "dark"],
            index=["light", "dark"].index(settings["config_screen"]),
            key="config_screem"
        )
        
        #--------- Ativar/desativar download ----------#
        download_enabled = st.selectbox(
            "Ativar download",
            ["Ativar", "Desativar"],
            index=0 if settings["config_download"] else 1,
            key="config_download"
        )
        
        #------- Configurar manutenção --------#
        maintenance_enabled = st.selectbox(
            "Configurar manutenção",
            ["Ativar", "Desativar"],
            index=0 if settings["config_maintenance"] else 1,
            key="config_maintenance"
        )
        
        #-------- Botão para salvar -----------#
        if st.button("Salvar alterações"):
            settings["config_screem"] = template_color
            settings["config_download"] = download_enabled == "Ativar"
            settings["config_maintenance"] = maintenance_enabled == "Ativar"
            save_settings(settings)
            
        #--------- Botão logout ------#
        if st.button("Logout"):
            # Remove a informação de login do session_state
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state['page'] = 'home'
            st.success("Você foi deslogado com sucesso.")
            st.rerun()

