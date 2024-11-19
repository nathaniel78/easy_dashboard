import threading
import time
import logging
from api.tasks import run_sql_and_data
from django.conf import settings

logger = logging.getLogger(__name__)

SYNC_TIME = settings.SYNC_TIME

def start_scheduler():
    # Chamar tasks
    def run_periodically():
        while True:
            try:
                run_sql_and_data()
                logger.info("Tarefa run_sql_and_data executada com sucesso.")
            except Exception as e:
                logger.error(f"Erro ao executar a tarefa: {e}")
            time.sleep(SYNC_TIME)

    thread = threading.Thread(target=run_periodically, daemon=True)
    thread.start()