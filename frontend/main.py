import streamlit as st
from src.pages import home, detail
from src.pages.admin import render_admin
from src.pages.login import render_login


def render_page():
    #------- Forçar estar logado para acessar admin ------#
    if st.session_state.get('page') == 'admin':
        #------- Verifica se o usuário está logado ------#
        if 'logged_in' not in st.session_state or not st.session_state['logged_in']:

            st.warning("Você precisa fazer login para acessar esta página.")
            if render_login():
                st.session_state['page'] = 'admin'
                render_admin()
        else:
            render_admin()

    elif st.session_state.get('page') == 'home':
        home.render_home()

    elif st.session_state.get('page') == 'detail':
        detail.render_detail()

    else:
        st.write("Página não encontrada.")

if __name__ == "__main__":
    from src.fragments.base import render_base
    render_base(render_page)

