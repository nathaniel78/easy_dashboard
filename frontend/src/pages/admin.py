import streamlit as st
from src.fragments.base import render_base
from src.core.config import (
    load_settings,
    save_settings,
    check_session_timeout
)


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
            key="config_screen"
        )
        
        #----------- Configurar cor dos gráficos ---------#
        template_chart_color = st.selectbox(
            "Configurar cor do gráfico",
            ["gray", "green", "mediumblue", "red", "yellow", "dark"],
            index=["gray", "green", "mediumblue", "red", "yellow", "dark"].index(settings["config_color"]),
            key="config_color"
        )
        
         #----------- Configurar size dos gráficos ---------#
        template_chart_size = st.selectbox(
            "Configurar comprimento (size) do gráfico",
            ["500", "700", "900"],
            index=["500", "700", "900"].index(settings["config_size"]),
            key="config_size"
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
        
        #------- Configurar token --------#
        token_input = st.text_input(
            "Digite o token de acesso:",
            value=settings.get("config_token", ""),
            key="config_token",
        )
        
        #------- Configurar refresh --------#
        refresh_input = st.text_input(
            "Digite o token de refresh:",
            value=settings.get("config_refresh", ""),
            key="config_refresh",
        )
        
        #-------- Botão para salvar -----------#
        if st.button("Salvar alterações"):
            settings["config_screen"] = template_color
            settings["config_color"] = template_chart_color
            settings["config_size"] = template_chart_size
            settings["config_download"] = download_enabled == "Ativar"
            settings["config_maintenance"] = maintenance_enabled == "Ativar"
            settings["config_token"] = token_input
            settings["config_refresh"] = refresh_input
            save_settings(settings)
            
        #--------- Botão logout ------#
        if st.button("Logout"):
            # Remove a informação de login do session_state
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state['page'] = 'home'
            st.success("Você foi deslogado com sucesso.")
            st.rerun()


#---------- Main ---------#
def main():
    render_base(render_admin)