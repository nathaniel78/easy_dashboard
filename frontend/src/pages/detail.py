# src/pages/detail.py
from src.fragments.base import render_base
from src.core.config import ConnectAPI
import streamlit as st
import plotly.express as px
from pathlib import Path
import pandas as pd
import json


#------ Load settings ---------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    with open(settings_path, "r") as file:
        settings = json.load(file)
    return settings

#------ Converte data ---------#
@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")

#------ Função para normalizar tipos ------#
def normalize_column_types(df):
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')  # Tenta converter para numérico, mas mantém texto se falhar
        except Exception as e:
            st.write(f"Erro ao converter coluna '{col}': {e}")
    return df

#--------- Detail ----------#
def render_detail():
    #---------- Session state sidebar -----------#
    description = st.session_state.get('description')
    id = st.session_state.get('id')
    type_chart = st.session_state.get('type_chart')
    #st.write(id)
    
    #----------- Conexao API ------------#
    api = ConnectAPI()
    
    response_data = api.get_data_as_result(id)
    
    st.subheader(f"Página: {description}")
    
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    is_download = settings["config_download"]
    
    #------------ Validação e Processamento de Dados -------------#
    if response_data and 'data_json' in response_data:
        data_json = response_data['data_json']
        data_name = response_data['name']

        # Transformar JSON em DataFrame
        df = pd.json_normalize(data_json)
        
        if not df.empty:
            # Normalizar tipos das colunas
            df = normalize_column_types(df)

            keys = list(df.columns)
            key0 = keys[0]
            other_keys = keys[1:]
            
            #------------ Gráficos ----------#
            if type_chart == 1:
                # Gráfico de barras empilhadas
                try:
                    bar_chart = px.bar(df, x=key0, y=other_keys, title=f'Gráfico de Barras: {data_name}', barmode='stack')
                    st.plotly_chart(bar_chart)
                except ValueError as e:
                    st.error(f"Erro ao criar gráfico de barras: {e}")
                
            elif type_chart == 2:
                # Gráfico de área empilhada
                if len(df[key0].unique()) > 1:
                    try:
                        area_chart = px.area(df, x=key0, y=other_keys, title=f'Gráfico de Área Empilhada: {data_name}')
                        st.plotly_chart(area_chart, use_container_width=True)
                    except ValueError as e:
                        st.error(f"Erro ao criar gráfico de área: {e}")
            
            elif type_chart == 3:
                # Gráfico de bolhas
                if len(other_keys) >= 2:
                    try:
                        bubble_chart = px.scatter(df, x=key0, y=other_keys[0], size=other_keys[1], color=key0, title=f'Gráfico de Bolhas: {data_name}')
                        st.plotly_chart(bubble_chart, use_container_width=True)
                    except ValueError as e:
                        st.error(f"Erro ao criar gráfico de bolhas: {e}")
                else:
                    st.warning("Não há colunas suficientes para criar um gráfico de bolhas.")

            # Botão para download do CSV
            if is_download:
                csv = convert_df(df)
                st.download_button(
                    label=f"Download do gráfico em CSV",
                    data=csv,
                    file_name=f"{data_name}.csv",
                    mime="text/csv",
                )
                
            elif type_chart == 4:
                # Gráfico de barras horizontais
                try:
                    horizontal_bar_chart = px.bar(df, x=other_keys, y=key0, orientation='h', title=f'Gráfico de Barras Horizontais: {data_name}')
                    st.plotly_chart(horizontal_bar_chart)
                    
                except ValueError as e:
                        st.error(f"Erro ao criar gráfico de bolhas: {e}")
                
                # Botão para download do CSV
                if is_download:
                    csv = convert_df(df)
                    st.download_button(
                        label=f"Download do gráfico em CSV",
                        data=csv,
                        file_name=f"{data_name}.csv",
                        mime="text/csv",
                    )
            
    else:
        st.error("Erro ao buscar ou processar os dados da API.")


#---------- Main ---------#
def main():
    render_base(render_detail)
