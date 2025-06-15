from django.urls import path
from . import views

app_name = 'carga_tct'

urlpatterns = [
    path('carga_tct/', views.carga_tct, name='carga_tct'),
    path('crear_registro/', views.crear_registro, name='crear_registro'),
    path('editar_registro/<int:registro_id>/', views.editar_registro, name='editar_registro'),
    path('eliminar_registro/<int:registro_id>/', views.eliminar_registro, name='eliminar_registro'),
]
