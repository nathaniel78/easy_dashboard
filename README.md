# Configurações do projeto

## Uso do Código:
Este código está disponível para uso com restrições comerciais e requer autorização para modificações.

- **Uso Pessoal e Não Comercial**: Permitido sem a necessidade de autorização.
- **Modificações e Uso Comercial**: Proibidos sem autorização prévia. Para modificações ou uso comercial, entre em contato com [nathanieljose78@gmail.com] para obter permissão.

## Sobre:
```
Easy dashboard é um aplicativo para criar gráficos de forma simplificada.
```

### Subindo projeto:
```
1 - Baixar o pacote git clone https://github.com/nathaniel78/easy_dashboard.git
2 - Rodar aplicação em docker, necessário ter instalado docker e docker-compose
3 - Copiar o arquivo .env.exemple dentro de docker para a raiz do projeto e configure os parametros
4 - Executando aplicação, dentro do diretorio tem o arquivo docker-compose.yml que subirá os container, para backend (django api_rest), frontend (streamlit), banco de dados (postgresql), pgadmin, nginx, com o comando docker-compose up -d --build.
5 - Url da api:
    5.1 - http://ip_do_host:8000/api/host/
    5.2 - http://ip_do_host:8000/api/sql/
    5.3 - http://ip_do_host:8000/api/data/
    5.4 - http://ip_do_host:8000/api/token/
    5.6 - http://ip_do_host:8000/api/token/refresh/
    5.7 - http://ip_do_host:8000/swagger/
    5.8 - http://ip_do_host:8000/redoc/
6 - Gerar usuário para acessar a api via web para gerar token, docker exec -it backend python manage.py createsuperuser, basta informar o username e password.
7 - Para acessar a area administrativa do frontend, como default o usuário é admin e a senha é 123 que podem e devem ser alteradas com o script reset.py, execute o comando docker exec -it frontend reset.py, informe o usuário e senha.
8 - Para o frontend fazer a comunicação com a api, deve ser gerado token e refresh, depois registrado no frontend na area administrativa.
9 - Caso necessite renovar o token, basta acessar na api o http://ip_do_host:8000/api/token/refresh/ e informar o token_refresh que será gerado um novo token.
```

### Registrando informações no backend:
```

Ainda em desenvolvimento, para realizar consultas diretamente no banco e salvar para consumo do frontend.
```

### Área administrativa do frontend:
```
1 - Acessando a área administrativa do frontend é possível configurar o template, habilitar o botão download para os gráficos, habilitar o aviso de manuteção, registrar o token e token refresh.

```