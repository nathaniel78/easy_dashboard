# src/pages/home.py
import streamlit as st
import plotly.express as px
import pandas as pd
from src.fragments.base import render_base

def render_home():
    st.write("Bem-vindo à página home!")

    # Exemplo de dados para os gráficos
    data = {
        "Categoria": ["A", "B", "C", "D"],
        "Valores": [23, 17, 35, 29]
    }
    df = pd.DataFrame(data)
    
    # Gráficos
    st.subheader("Gráfico de Barra Principal")
    bar_chart = px.bar(df, x="Categoria", y="Valores", title="Gráfico de Barra Principal")
    st.plotly_chart(bar_chart, use_container_width=True)
    
    st.subheader("Gráfico de Linha")
    line_chart = px.line(df, x="Categoria", y="Valores", title="Gráfico de Linha")
    st.plotly_chart(line_chart, use_container_width=True)
    
    st.subheader("Gráfico de Pizza")
    pie_chart = px.pie(df, names="Categoria", values="Valores", title="Gráfico de Pizza")
    st.plotly_chart(pie_chart, use_container_width=True)
    
    st.subheader("Outro Gráfico de Barra")
    bar_chart_2 = px.bar(df, x="Categoria", y="Valores", title="Outro Gráfico de Barra")
    st.plotly_chart(bar_chart_2, use_container_width=True)

def main():
    render_base(render_home)
