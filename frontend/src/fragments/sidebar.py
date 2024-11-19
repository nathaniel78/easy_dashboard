import streamlit as st
from src.core.config import ConnectAPI
import pandas as pd
from pathlib import Path
import json
from src.core.param import (
    IMAGE_LOGO
)

#-------- Carregar settings ----------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    
    if settings_path.exists():
        with open(settings_path, "r") as f:
            settings = json.load(f)
        return settings
    else:
        st.error("Arquivo de settings não encontrado.")
        return {}

#------- Sidebar -----------#
def render_sidebar():
    # ----------- Conexão API ------------ #
    api = ConnectAPI()
    response_data_list = api.get_data_as_list()
    
    # Validação inicial do response
    if response_data_list is not None and isinstance(response_data_list, list):
        try:
            dl = pd.json_normalize(response_data_list)
            dl = dl.sort_values(by="id", ascending=False)
        except Exception as e:
            st.error(f"Erro ao processar os dados da API: {e}")
            dl = pd.DataFrame()
    else:
        dl = pd.DataFrame()

    # Nome da coluna a ser utilizada
    column_name = "name"

    # ----------- Logo ----------- #
    st.sidebar.markdown(
        f"""
        <div class="img-logo">
            <img src="{IMAGE_LOGO}">
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------- Carrega as configurações do settings.json -------------- #
    settings = load_settings()

    maintenance = settings.get("config_maintenance", False)

    # ----------- Menu ------------ #
    st.sidebar.title("Menu")

    if not maintenance:
        # Define a página principal se não estiver definida
        if 'page' not in st.session_state:
            st.session_state['page'] = 'home'

        # Botão para a página inicial
        if st.sidebar.button("Home"):
            st.session_state['page'] = 'home'

        # Itera pelos dados validados
        if not dl.empty and column_name in dl.columns:
            for index, row in dl.iterrows():
                try:
                    # Obtém os valores das colunas necessárias com validação
                    value_id = row.get(0, None)
                    value_name = row.get(1, "Sem Nome")
                    value_type_chart = row.get(4, "Tipo Desconhecido")
                    
                    # Limita o comprimento do nome para exibição
                    value_name_limite = value_name[:40]

                    # Cria o botão com uma chave única baseada no índice
                    if st.sidebar.button(f"{value_name_limite}", key=f"button_{index}"):
                        st.session_state['id'] = value_id
                        st.session_state['page'] = 'detail'
                        st.session_state['description'] = value_name
                        st.session_state['type_chart'] = value_type_chart
                except Exception as e:
                    st.warning(f"Erro ao processar o item {index}: {e}")

    # Botão para acessar a página Admin
    if st.sidebar.button("Admin"):
        st.session_state['page'] = 'admin'
