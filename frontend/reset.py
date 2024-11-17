from pathlib import Path
import json

#-------- Salvar settings ---------#
def save_settings(new_credentials):
    credentials_path = Path("src/core/authentication.json")
    
    with open(credentials_path, "w") as f:
        json.dump(new_credentials, f, indent=4)
    print("Configurações salvas com sucesso!")

#--------- Alterar credenciais ----------#
def input_credentials(username, password):
    if not username or not password:  # Verifica se ambos são fornecidos
        print("Precisa informar usuário e senha.")
        return

    # Caminho do arquivo JSON
    credentials_path = Path("src/core/authentication.json")

    # Carregar credenciais existentes ou criar um novo arquivo
    if credentials_path.exists():
        with open(credentials_path, "r") as f:
            credentials = json.load(f)
    else:
        credentials = {}

    # Atualizar as credenciais
    credentials["username"] = username
    credentials["password"] = password

    # Salvar as credenciais atualizadas
    save_settings(credentials)

#--------- Main ---------#
if __name__ == "__main__":
    username = input("Informe o novo usuário: ")
    password = input("Informe a nova senha: ")
    input_credentials(username, password)
