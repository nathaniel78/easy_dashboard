# src/fragments/header.py
import streamlit as st
from src.core.config import (
    load_settings
)

#--------- Header ----------#
def render_header():
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    is_maintenance = settings["config_maintenance"]
    
    if is_maintenance is not True:
        st.markdown("<h1 style='text-align: center;'>Dashboard</h1>", unsafe_allow_html=True)
