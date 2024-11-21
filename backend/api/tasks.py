from celery import shared_task
from api.execute_query import SQLTaskRunner

 # TODO: Function run_sql_and_data
@shared_task
def run_sql_and_data():
    # Chamar as funções para atualização do sql e json de consulta
    SQLTaskRunner.run_sql()
    SQLTaskRunner.run_data()