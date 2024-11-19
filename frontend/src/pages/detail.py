from typing import Self
import plotly.io as pio
pio.renderers.default = "browser"

from src.fragments.base import render_base
from src.core.config import ConnectAPI
import streamlit as st
import plotly.express as px
from pathlib import Path
import pandas as pd
import json
from src.core.param import (
    CHART_WIDTH,
    CHART_HEIGHT,
)


#-------- Carregar settings ----------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    
    if settings_path.exists():
        with open(settings_path, "r") as f:
            settings = json.load(f)
        return settings
    else:
        st.error("Arquivo de settings não encontrado.")
        return {}

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
                bar_chart = px.bar(df, x=key0, y=other_keys, title=f'Gráfico de Barras: {data_name}', barmode='stack')
                    
                bar_chart.update_layout(
                    width=CHART_WIDTH,
                    height=CHART_HEIGHT,
                    margin=dict(l=0, r=0, t=40, b=0)
                )
                
                st.plotly_chart(bar_chart)
                
            elif type_chart == 2:
                # Gráfico de área empilhada
                area_chart = px.area(df, x=key0, y=other_keys, title=f'Gráfico de Área Empilhada: {data_name}')
                        
                area_chart.update_layout(
                    width=CHART_WIDTH,
                    height=CHART_HEIGHT,
                    margin=dict(l=0, r=0, t=40, b=0) 
                )
                
                st.plotly_chart(area_chart, use_container_width=True)
                    
            
            elif type_chart == 3:
                # Gráfico de bolhas
                bubble_chart = px.scatter(df, x=key0, y=other_keys[0], size=other_keys[1], color=key0, title=f'Gráfico de Bolhas: {data_name}')
                        
                bubble_chart.update_layout(
                    width=CHART_WIDTH,
                    height=CHART_HEIGHT,
                    margin=dict(l=0, r=0, t=40, b=0) 
                )
                
                st.plotly_chart(bubble_chart, use_container_width=True)

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
                horizontal_bar_chart = px.bar(df, x=other_keys, y=key0, orientation='h', title=f'Gráfico de Barras Horizontais: {data_name}')
                    
                horizontal_bar_chart.update_layout(
                        width=CHART_WIDTH,
                        height=CHART_HEIGHT,
                        margin=dict(l=0, r=0, t=40, b=0) 
                    )
                
                st.plotly_chart(horizontal_bar_chart)
                
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
