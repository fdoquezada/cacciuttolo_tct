from django.apps import AppConfig

class CargaTctConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carga_tct'
    verbose_name = 'Gestión de Combustible'
    
    def ready(self):
        print('CargaTctConfig ready')
