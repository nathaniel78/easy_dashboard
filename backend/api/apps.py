from django.apps import AppConfig


# TODO: Class apliconfig
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # TODO: Scheduled execution for execute_query
    def ready(self):
        from api.scheduler import start_scheduler
        start_scheduler()
