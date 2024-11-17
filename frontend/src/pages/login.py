import streamlit as st
from pathlib import Path
import json


#-------- Carregando credentials ---------#
def load_credentials():
    credentials_path = Path("src/core/authentication.json")
    
    if credentials_path.exists():
        with open(credentials_path, "r") as f:
            credentials = json.load(f)
        return credentials
    else:
        st.error("Arquivo de credenciais não encontrado.")
        return None

#-------- Credentials ---------#
def render_login():
    st.title("Login")
    
    #------- Carrega as credenciais do arquivo ---------#
    credentials = load_credentials()
    if not credentials:
        return False
    
    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        #-------- Validar credencias ---------#
        if username == credentials["username"] and password == credentials["password"]:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state['page'] = 'admin'
            st.success("Login bem-sucedido!")
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")
    
    return False
