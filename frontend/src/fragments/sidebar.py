import streamlit as st
from src.core.config import ConnectAPI
import pandas as pd
from src.core.param import IMAGE_LOGO
from src.core.config import load_settings
import logging
logging.basicConfig(level=logging.DEBUG)

#------- Sidebar -----------#
def render_sidebar():
    # ----------- Conexão API ------------ #
    try:
        api = ConnectAPI()
        response_data_list = api.get_data_as_list()
        logging.debug(f"Dados retornados pela API em sidebar: {response_data_list}")
    except Exception as e:
        st.error(f"Erro ao conectar-se à API: {e}")
        logging.error(f"Erro ao conectar-se à API em sidebar: {e}")
        response_data_list = []

    # Validação inicial dos dados da API
    if response_data_list and isinstance(response_data_list, list):
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
                    value_id = row.get('id', None)
                    value_name = row.get('name', "Sem Nome")
                    value_type_chart = row.get('type_chart', "Tipo Desconhecido")

                    # Limita o comprimento do nome para exibição
                    value_name_limit = value_name[:40]

                    # Cria o botão com uma chave única baseada no índice
                    if st.sidebar.button(f"{value_name_limit}", key=f"button_{index}"):
                        st.session_state['id'] = value_id
                        st.session_state['page'] = 'detail'
                        st.session_state['description'] = value_name
                        st.session_state['type_chart'] = value_type_chart
                except Exception as e:
                    st.warning(f"Erro ao processar o item {index}: {e}")

    # Botão para acessar a página Admin
    if st.sidebar.button("Admin"):
        st.session_state['page'] = 'admin'
