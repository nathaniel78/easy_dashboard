#--------------- BACKEND --------------#
FROM python:3.12-slim as backend

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /api

# Instalar dependências do sistema necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev python3-dev build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Atualizar pip
RUN pip install --upgrade pip

# Copiar e instalar dependências Python
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o pacote datasets
RUN pip install -U datasets

# Copiar código fonte
COPY backend /api

EXPOSE 8000

#--------------- FRONTEND --------------#
FROM python:3.12-slim as frontend

# Definir variáveis de ambiente para codificação
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Definindo o diretório de trabalho
WORKDIR /dashboard

# Instalar dependências do sistema necessárias, incluindo curl e ping
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev python3-dev build-essential curl iputils-ping && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Atualizar pip
RUN pip install --upgrade pip

# Copiar e instalar dependências Python
COPY ./requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Atualizar pandas explicitamente
RUN pip install --no-cache-dir pandas

# Instalar o pacote datasets
RUN pip install -U datasets

# Copiar o código fonte do frontend
COPY frontend /dashboard

# Garantir permissões adequadas para o diretório /dashboard
RUN chmod -R 777 /dashboard

# Definindo o usuário root para garantir permissões adequadas
USER root

# Expondo a porta do contêiner para comunicação
EXPOSE 8501

# Comando para verificar a saúde do contêiner
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


