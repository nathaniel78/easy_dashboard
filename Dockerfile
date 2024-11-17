#--------------- BACKEND --------------#
# Use uma imagem base do Python 3.12
FROM python:3.12 as backend

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
FROM python:3.12 as frontend

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

# Copia o restante do código do projeto para o contêiner
COPY frontend /dashboard

# Expõe a porta 8501
EXPOSE 8501
