# src/fragments/header.py
import streamlit as st

#--------- Header ----------#
def render_header():
    st.markdown("<h1 style='text-align: center;'>Dashboard</h1>", unsafe_allow_html=True)
