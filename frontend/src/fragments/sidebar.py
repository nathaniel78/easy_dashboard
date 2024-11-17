import streamlit as st
from src.core.config import ConnectAPI
import pandas as pd
from pathlib import Path
import json
from src.core.param import (
    IMAGE_LOGO
)

#------ Load settings ---------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    with open(settings_path, "r") as file:
        settings = json.load(file)
    return settings

#------- Sidebar -----------#
def render_sidebar():
    #----------- Conexao API ------------#
    api = ConnectAPI()
    
    response_data_list = api.get_data_as_list()
    
    data_list = response_data_list
    
    dl = pd.json_normalize(data_list)
    
    column_name = "name"
    
    #----------- Logo -----------#
    st.sidebar.markdown(
        f"""
        <div class="img-logo">
            <img src="{IMAGE_LOGO}">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    maintenance = settings["config_maintenance"]  

    #----------- Menu ------------#
    st.sidebar.title("Menu")
    
    if maintenance is not True:
        # Definindo as páginas principal
        if 'page' not in st.session_state:
            st.session_state['page'] = 'home'
        
        if st.sidebar.button("Home"):
            st.session_state['page'] = 'home'
        
        if column_name in dl.columns:
            for index, row in dl.iterrows():
                # Obtendo o valor da coluna 'name'
                value_id = row[0]
                value_name = row[1]
                value_type_chart = row[5]
                value_name_limite = value_name[0:40]

                # Botão com uma chave única baseada no índice
                if st.sidebar.button(f"{value_name_limite}", key=f"button_{index}"):
                    st.session_state['id'] = value_id
                    st.session_state['page'] = 'detail'
                    st.session_state['description'] = value_name
                    st.session_state['type_chart'] = value_type_chart
                
    # Botão para acessar a página Admin
    if st.sidebar.button("Admin"):
        st.session_state['page'] = 'admin'
