from django.utils import timezone
from django.shortcuts import get_object_or_404
from api.models import SQL, Data
from api.services import DatabaseService
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SQLTaskRunner:
    @staticmethod
    def run_sql():
        sql_entries = SQL.objects.all()

        for entry in sql_entries:
            host = entry.host            

            if not host.host_active:
                logger.info(f"Host '{host.name}' está inativo. Ignorando execução.")
                continue

            try:
                db_service = DatabaseService(host.id)
            except Exception as e:
                logger.error(f"Erro ao inicializar DatabaseService para Host '{host.name}': {e}")
                continue

            if not db_service.test_connection():
                logger.error(f"Falha ao conectar ao banco de dados para o Host '{host.name}'. Ignorando execução.")
                continue

            query = entry.sql
            try:
                results = db_service.execute_query(query)
                logger.debug(f"Resultado da consulta para '{entry.name}': {results}")

                if results is None:
                    logger.warning(f"Consulta para '{entry.name}' retornou nenhum resultado.")
                    continue
            except Exception as e:
                logger.error(f"Erro ao executar consulta para '{entry.name}': {e}")
                continue

            try:
                if results:
                    results_json = json.dumps(results, ensure_ascii=False)
                    entry.result = results_json
                    entry.data_update = timezone.now()
                    entry.save()
                    logger.info(f"Consulta '{entry.name}' executada com sucesso.")
                else:
                    logger.warning(f"Consulta para '{entry.name}' não gerou resultados.")
            except Exception as e:
                logger.error(f"Erro ao salvar resultados para '{entry.name}': {e}")

    @staticmethod
    def run_data():
        data_entries = Data.objects.all()

        for data_update in data_entries:
            sql_id = data_update.sql.id
            logger.debug(f"Processando o Data de id: {data_update.id}, com SQL de id: {sql_id}")

            try:
                # Obtém o objeto SQL correspondente ao ID
                sql_result = get_object_or_404(SQL, pk=sql_id)
                
                # Verifica se o campo 'result' do SQL não é vazio
                if sql_result.result:
                    # Atribui o valor de 'result' do SQL para o campo 'data_json' do Data
                    data_update.data_json = sql_result.result
                    data_update.save()  # Salva o objeto Data com a atualização
                    logger.info(f"Data com ID {data_update.id} atualizado com sucesso.")
                else:
                    logger.warning(f"SQL de ID {sql_id} não contém resultado para o Data com ID {data_update.id}.")
            
            except Exception as e:
                logger.error(f"Erro ao atualizar Data com ID {data_update.id}: {e}")