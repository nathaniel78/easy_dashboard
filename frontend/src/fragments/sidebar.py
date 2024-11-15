import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

def render_sidebar():
    IMAGE_LOGO = os.getenv(
        "IMAGE_LOGO_URL", 
        default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Instituto_Federal_do_Amazonas_-_Marca_Vertical_2015.svg/800px-Instituto_Federal_do_Amazonas_-_Marca_Vertical_2015.svg.png"
        )

    # Adiciona o HTML com CSS inline para centralizar a imagem
    st.sidebar.markdown(
        f"""
        <div class="img-logo">
            <img src="{IMAGE_LOGO}">
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.title("Menu")
    
    # Definindo as páginas
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'
    
    # Navegação por botões
    if st.sidebar.button("Home"):
        st.session_state['page'] = 'home'
        
    if st.sidebar.button("Detail"):
        st.session_state['id'] = 2
        st.session_state['page'] = 'detail'
        st.session_state['description'] = 'Página padrão detail'
    
    PAGES_SQL = ['Total alunos', 'Total de servidores']
    
    # Iterando diretamente sobre a lista de páginas com índice
    for idx, name_page in enumerate(PAGES_SQL):
        if st.sidebar.button(f"{name_page}"):
            st.session_state['id'] = idx
            st.session_state['page'] = 'detail'
            st.session_state['description'] = name_page