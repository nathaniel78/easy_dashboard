# src/fragments/header.py
import streamlit as st
from pathlib import Path
import json

#------ Load settings ---------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    with open(settings_path, "r") as file:
        settings = json.load(file)
    return settings

#--------- Header ----------#
def render_header():
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    is_maintenance = settings["config_maintenance"]
    
    if is_maintenance is not True:
        st.markdown("<h1 style='text-align: center;'>Dashboard</h1>", unsafe_allow_html=True)
