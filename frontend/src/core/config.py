import requests
import streamlit as st
from pathlib import Path
import json
import os

#-------- Carregar settings ----------#
def load_settings():
    settings_path = Path("src/core/settings.json")
    
    if settings_path.exists():
        with open(settings_path, "r") as f:
            settings = json.load(f)
        return settings
    else:
        st.error("Arquivo de settings não encontrado.")
        return None

#---------- Classe ConnectAPI ---------#
class ConnectAPI:
    def __init__(self):
        self.API_URL = os.getenv(
            "API_URL", 
            default='http://localhost:8000/api'
        )
    
    def load_tokens(self):
        settings = load_settings()
        return settings.get("config_token", ""), settings.get("config_refresh", "")
    
    def connect_host(self):
        token, refresh_token = self.load_tokens()
        headers = {
            'Authorization': f'Bearer {token}',
            'Refresh-Token': refresh_token
        }

        try:
            response = requests.get(self.API_URL, headers=headers)
            response.raise_for_status()
            print("Conexão bem-sucedida!")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar-se à API: {e}")
            return None

    def get_data_as_result(self, pk):
        token, refresh_token = self.load_tokens()
        headers = {
            'Authorization': f'Bearer {token}',
            'Refresh-Token': refresh_token 
        }
        
        api_endpoint = f"/data/{pk}"
        try:
            response = requests.get(self.API_URL + api_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados em data com ID {pk}: {e}")
            return None
    
    def get_data_as_list(self):
        token, refresh_token = self.load_tokens()
        headers = {
            'Authorization': f'Bearer {token}',
            'Refresh-Token': refresh_token
        }
        
        api_endpoint = "/data/"
        try:
            response = requests.get(self.API_URL + api_endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar a lista em data: {e}")
            return None


