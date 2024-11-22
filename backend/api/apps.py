from django.apps import AppConfig
from django.conf import settings
import sys

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Evite inicialização se não for o comando 'runserver'
        if 'runserver' not in sys.argv:
            return

        # Habilita o scheduler somente se a variável de ambiente permitir
        if settings.ENABLE_SCHEDULER == 'True':
            try:
                from api.scheduler import start_scheduler
                start_scheduler()
            except Exception as e:
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Erro ao inicializar o scheduler: {e}")
