import streamlit as st
from src.pages import home, detail  # Importe suas páginas aqui

# Renderizando o conteúdo com base na página selecionada
def render_page():
    if st.session_state['page'] == 'home':
        home.render_home()  # Função que renderiza a página Home
    elif st.session_state['page'] == 'detail':
        detail.render_detail()  # Função que renderiza a página Detalhes

if __name__ == "__main__":
    # Carrega a estrutura principal do layout e chama a página correta
    from src.fragments.base import render_base
    render_base(render_page)
