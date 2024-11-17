from src.fragments.base import render_base
from src.core.config import ConnectAPI
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
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

#------ Home ---------#
def render_home():
    #------------ Conexão com a API ------------#
    api = ConnectAPI()
    response_data_list = api.get_data_as_list()
    
    
    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    
    is_download = settings["config_download"]

    #--------- Validação -----------#
    if not response_data_list:
        st.write("Nenhum dado encontrado.")
        return

    dl = pd.json_normalize(response_data_list)
    values = list(dl.values)

    max_graphs = 4
    limited_values = values[::-1][:max_graphs]

    for i, value in enumerate(limited_values):
        value_id = value[0]
        value_name = value[1]
        value_emphasis = value[6]
        data_type_chart = value[5]

        if value_emphasis:
            response_data = api.get_data_as_result(value_id)
            data_json = response_data.get('data_json')

            if data_json:
                try:
                    df = pd.json_normalize(data_json)
                    keys = list(df.columns)
                    
                    if len(keys) < 2:
                        st.write(f"Colunas insuficientes para criar gráficos para {value_name}.")
                        continue

                    key0 = keys[0]
                    other_keys = keys[1:]

                    #-------- Gerar gráficos com base no tipo -------#
                    if data_type_chart == 1:
                        # Gráfico de barras empilhadas
                        bar_chart = px.bar(df, x=key0, y=other_keys, title=f'Gráfico de Barras: {value_name}', barmode='stack')
                        st.plotly_chart(bar_chart)
                        
                        if is_download is True:
                            csv = convert_df(df)
                            
                            st.download_button(
                                label=f"Download do gráfico em CSV",
                                data=csv,
                                file_name=f"{value_name}.csv",
                                mime="text/csv",
                            )

                    elif data_type_chart == 2:
                        # Gráfico de área empilhada
                        if len(df[key0].unique()) > 1:
                            area_chart = px.area(df, x=key0, y=other_keys, title=f'Gráfico de Área Empilhada: {value_name}')
                            st.plotly_chart(area_chart)
                            
                            if is_download is True:
                                csv = convert_df(df)
                                
                                st.download_button(
                                    label=f"Download do gráfico em CSV",
                                    data=csv,
                                    file_name=f"{value_name}.csv",
                                    mime="text/csv",
                                )

                    elif data_type_chart == 3:
                        # Gráfico de bolhas empilhadas
                        if len(other_keys) >= 2:
                            bubble_chart = px.scatter(df, x=key0, y=other_keys[0], size=other_keys[1], color=key0,
                                                      title=f'Gráfico de Bolhas Empilhadas: {value_name}')
                            st.plotly_chart(bubble_chart)
                            
                            if is_download is True:
                                csv = convert_df(df)
                                
                                st.download_button(
                                    label=f"Download do gráfico em CSV",
                                    data=csv,
                                    file_name=f"{value_name}.csv",
                                    mime="text/csv",
                                )
                            
                        else:
                            st.write(f"Não há colunas suficientes para criar um gráfico de bolhas para {value_name}.")
                except Exception as e:
                    st.write(f"Erro ao processar os dados para {value_name}: {e}")
                    continue
            else:
                st.write(f"Dados JSON ausentes para {value_name}.")


#---------- Main ---------#
def main():
    render_base(render_home)
        
