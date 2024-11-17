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

#--------- Detail ----------#
def render_detail():
    #---------- Session state sidebar -----------#
    description = st.session_state.get('description')
    id = st.session_state.get('id')
    type_chart = st.session_state.get('type_chart')
    st.write(id)
    
    #----------- Conexao API ------------#
    api = ConnectAPI()
    
    response_data = api.get_data_as_result(id)
    
    data_json = response_data['data_json']

    df = pd.json_normalize(data_json)
    
    st.subheader(f"Página: {description}")
    
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    is_download = settings["config_download"]
    
    #------------ Validação -------------#
    if response_data and 'data_json' in response_data:
        data_json = response_data['data_json']
        data_name = response_data['name']

        df = pd.json_normalize(data_json)

        if not df.empty:
            keys = list(df.columns)

            for i, key in enumerate(keys):
                # st.write(f"Chave {i+1}: {key}")
                key0 = keys[0]
                other_keys = keys[1:]
            
            #------------ Gráficos ----------#
            if type_chart == 1:
                # Criando o gráfico de barras empilhadas com as chaves restantes
                bar_chart = px.bar(df, x=key0, y=other_keys, title=f'Gráfico de barras: {data_name}', barmode='stack')

                st.plotly_chart(bar_chart)
                
                if is_download is True:
                    csv = convert_df(df)
                    
                    st.download_button(
                        label=f"Download do gráfico em CSV",
                        data=csv,
                        file_name=f"{data_name}.csv",
                        mime="text/csv",
                    )
            
            elif type_chart == 2:
                # Verificando se há múltiplas linhas para o gráfico de linha
                if len(df[key0].unique()) > 1:
                    # Criando o gráfico de área empilhada
                    area_chart = px.area(df, x=key0, y=other_keys, title=f'Gráfico de Área Empilhada: {data_name}')
                    
                    st.plotly_chart(area_chart, use_container_width=True)
                    
                    if is_download is True:
                        csv = convert_df(df)
                        
                        st.download_button(
                            label=f"Download do gráfico em CSV",
                            data=csv,
                            file_name=f"{data_name}.csv",
                            mime="text/csv",
                        )
                    
            elif type_chart == 3:
                if len(other_keys) >= 2:
                    # Criando o gráfico de bolhas empilhadas, se houver ao menos duas chaves
                    bubble_chart = px.scatter(df, x=key0, y=other_keys[0], size=other_keys[1], color=key0, title=f'Gráfico de Bolhas Empilhadas: {data_name}')
                    
                    st.plotly_chart(bubble_chart, use_container_width=True)
                    
                    if is_download is True:
                        csv = convert_df(df)
                        
                        st.download_button(
                            label=f"Download do gráfico em CSV",
                            data=csv,
                            file_name=f"{data_name}.csv",
                            mime="text/csv",
                        )
                    
                else:
                    # Exibindo erro quando não há colunas suficiente para gerar gráfico. Obs.: colocar aviso no admin
                    st.write("Não há colunas suficientes para criar um gráfico de bolhas empilhadas.")
        

    else:
        st.write("Erro ao buscar ou processar os dados da API.")


#---------- Main ---------#
def main():
    render_base(render_detail)
