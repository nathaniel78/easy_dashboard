import os
from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        if os.getenv('ENABLE_SCHEDULER', 'false') == 'true':
            from api.scheduler import start_scheduler
            start_scheduler()
