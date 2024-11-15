import requests


# Classe ConnectAPI
class ConnectAPI:
    # URL base da API
    API_URL = "http://localhost:8000/api"
    
    # Método para conectar ao host com ID específico
    def connect_host(self, pk):
        api_host = f'/host/detail/{pk}'
        try:
            response = requests.get(self.API_URL + api_host)
            response.raise_for_status()
            host = response.json()
            return host
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar-se à API: {e}")
            return None
