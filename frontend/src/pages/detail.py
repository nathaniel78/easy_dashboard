# src/pages/detail.py
import streamlit as st
import plotly.express as px
import pandas as pd
from src.fragments.base import render_base

def render_detail():
    page = st.session_state.get('page')
    description = st.session_state.get('description')
    id = st.session_state.get('id')
    st.write(id)
    st.write("Página de Detalhes")
    
    # Exemplo de dados para os gráficos
    data = {
        "Categoria": ["A", "B", "C", "D"],
        "Valores": [23, 17, 35, 29]
    }
    df = pd.DataFrame(data)
    
    if id == 0:
        st.subheader("Gráfico de Barra Principal")
        bar_chart = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barra Principal")
        st.plotly_chart(bar_chart, use_container_width=True)
    
    elif id == 1:
        st.subheader("Gráfico de Linha")
        line_chart = px.line(df, x="Categoria", y="Valores", title="Gráfico de Linha")
        st.plotly_chart(line_chart, use_container_width=True)
        
    elif id == 2:
        st.subheader("Gráfico de Pizza")
        pie_chart = px.pie(df, names="Categoria", values="Valores", title="Gráfico de Pizza")
        st.plotly_chart(pie_chart, use_container_width=True)
    
    else:
        st.write("Página não encontrada")

def main():
    render_base(render_detail)
