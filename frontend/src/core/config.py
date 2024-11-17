import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

#---------- Classe ConnectAPI ---------#
class ConnectAPI:
    #-------- URL base da API ---------#
    API_URL = os.getenv(
        "API_URL", 
        default='http://localhost:8000/api'
    )
    # API_URL = "http://backend:8000/api"
    
    #------- Método para conectar ao host e validar a conexão -------#
    def connect_host(self):
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            print("Conexão bem-sucedida!")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar-se à API: {e}")
            return None

    #------- Método para buscar dados de uma entidade específica por ID --------#
    def get_data_as_result(self, pk):
        api_endpoint = f"/data/{pk}"
        try:
            response = requests.get(self.API_URL + api_endpoint)
            response.raise_for_status()
            data = response.json() 
            return data
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados em data com ID {pk}: {e}")
            return None
        
    
    #------ Método para buscar uma lista --------#
    def get_data_as_list(self):
        api_endpoint = f"/data/"
        try:
            response = requests.get(self.API_URL + api_endpoint)
            response.raise_for_status()
            data = response.json() 
            return data
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar a lista em data: {e}")
            return None
