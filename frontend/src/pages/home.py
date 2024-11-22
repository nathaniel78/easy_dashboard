from src.fragments.base import render_base
from src.core.config import ConnectAPI
import streamlit as st
import pandas as pd
import plotly.express as px
from src.core.config import load_settings
import logging
logging.basicConfig(level=logging.DEBUG)


#------ Converte data ---------#
@st.cache_data
def convert_df(df):
    return df.to_csv().encode("utf-8")


#------ Home ---------#
def render_home():
    #------------ Conexão com a API ------------#
    try:
        # Inicializa a conexão com a API
        api = ConnectAPI()
        response_data_list = api.get_data_as_list()
        logging.debug(f"Dados retornados pela API em home: {response_data_list}")
    except Exception as e:
        # Trata exceções ao tentar conectar-se à API
        st.error(f"Erro ao conectar-se à API: {e}")
        logging.error(f"Erro ao conectar-se à API em home: {e}")
        return

    #---------- Carrega as configurações do settings.json --------------#
    settings = load_settings()
    is_download = settings.get("config_download", False)

    #--------- Validação -----------#
    if not response_data_list or not isinstance(response_data_list, list):
        st.warning("A API retornou uma lista vazia ou dados inválidos.", icon="⚠️")
        logging.warning(f"Resposta inválida da API: {response_data_list}")
        return
    
    try:
        dl = pd.json_normalize(response_data_list)
        dl = dl.sort_values(by="id", ascending=True)  # Ordena pelo campo "id"
        values = list(dl.values)
        logging.debug(f"Dados processados com sucesso: {dl.head()}")
    except Exception as e:
        st.error(f"Erro ao processar os dados da API: {e}")
        logging.error(f"Erro ao processar os dados da API: {e}")
        dl = pd.DataFrame()

    max_graphs = 4
    limited_values = values[::-1][:max_graphs]

    for i, value in enumerate(limited_values):
        try:
            value_id = value[0]
            value_name = value[1]
            value_emphasis = value[5]
            data_type_chart = value[4]

            if value_emphasis:
                response_data = api.get_data_as_result(value_id)
                data_json = response_data.get("data_json")

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
                            bar_chart = px.bar(df, x=key0, y=other_keys, 
                                title=f"Gráfico de Barras: {value_name}", barmode="stack",
                                color_discrete_sequence=[settings["config_color"]]
                            )
                                                                                   
                            bar_chart.update_layout(
                                width=int(settings["config_size"])                                
                            )
                            
                            st.plotly_chart(bar_chart)

                            if is_download:
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
                                area_chart = px.area(df, x=key0, y=other_keys, 
                                    title=f"Gráfico de Área Empilhada: {value_name}",
                                    color_discrete_sequence=[settings["config_color"]]
                                )
                                                               
                                area_chart.update_layout(
                                    width=int(settings["config_size"]) 
                                )
                                
                                st.plotly_chart(area_chart)

                                if is_download:
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
                                bubble_chart = px.scatter(
                                    df, x=key0, y=other_keys[0], size=other_keys[1], color=key0, 
                                        title=f"Gráfico de Bolhas: {value_name}",
                                        color_discrete_sequence=[settings["config_color"]]
                                )
                                                                
                                bubble_chart.update_layout(
                                    width=int(settings["config_size"])
                                )
                                
                                st.plotly_chart(bubble_chart)

                                if is_download:
                                    csv = convert_df(df)
                                    st.download_button(
                                        label=f"Download do gráfico em CSV",
                                        data=csv,
                                        file_name=f"{value_name}.csv",
                                        mime="text/csv",
                                    )
                            else:
                                st.write(f"Não há colunas suficientes para criar um gráfico de bolhas para {value_name}.")
                                
                        #-------- Gerar gráficos de barra horizontal -------#
                        elif data_type_chart == 4:
                            # Gráfico de barras horizontal
                            df = df.sort_values(by=other_keys, ascending=True) # sort ascendente caso queira alterar mude para False
                            
                            horizontal_bar_chart = px.bar(df, x=other_keys, y=key0, orientation='h', 
                                title=f'Gráfico de Barras Horizontais: {value_name}', 
                                color_discrete_sequence=[settings["config_color"]]
                            )
                                                        
                            horizontal_bar_chart.update_layout(
                                    width=int(settings["config_size"])
                                )

                            st.plotly_chart(horizontal_bar_chart)
                            
                            if is_download:
                                csv = convert_df(df)
                                st.download_button(
                                    label=f"Download do gráfico em CSV",
                                    data=csv,
                                    file_name=f"{value_name}.csv",
                                    mime="text/csv",
                                )
                        
                    except Exception as e:
                        st.error(f"Erro ao processar os dados para {value_name}: {e}")
                        continue
                else:
                    st.write(f"Dados JSON ausentes para {value_name}.")
        except Exception as e:
            st.error(f"Erro ao processar a entrada {i + 1}: {e}")


#---------- Main ---------#
def main():
    render_base(render_home)
