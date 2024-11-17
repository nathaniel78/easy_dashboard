#--------------- BACKEND --------------#
# Use uma imagem base do Python 3.12
FROM python:3.12-slim as backend

# Define o diretório de trabalho
WORKDIR /api

# Instala as dependências do sistema necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt para o contêiner
COPY ./requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto para o contêiner
COPY backend /api

# Expõe a porta 8000
EXPOSE 8000

#--------------- FRONTEND --------------#
# Use uma imagem base do Python 3.12
FROM python:3.12-slim as frontend

# Define o diretório de trabalho
WORKDIR /dashboard

# Instala as dependências do sistema necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt para o contêiner
COPY ./requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Atualize pandas explicitamente
RUN pip install --no-cache-dir pandas

# Garanta que o usuário tenha permissões adequadas
RUN chmod -R 755 /dashboard

# Copia o restante do código do projeto para o contêiner
COPY frontend /dashboard

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
