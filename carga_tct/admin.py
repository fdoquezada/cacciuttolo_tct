from django.contrib import admin
from .models import RegistroCombustible

@admin.register(RegistroCombustible)
class RegistroCombustibleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha',
        'patente',
        'guia',
        'estacion_servicio',
        'suministro',
        'kilometraje',
        'consumo_litros',
        'fecha_registro'
    )
    list_filter = (
        'fecha',
        'suministro',
        'estacion_servicio',
        'patente'
    )
    search_fields = (
        'patente',
        'guia',
        'estacion_servicio'
    )
    ordering = ('-fecha', '-fecha_registro')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Información Básica', {
            'fields': (
                'fecha',
                'patente',
                'guia',
                'estacion_servicio',
                'suministro'
            )
        }),
        ('Mediciones', {
            'fields': (
                'kilometraje',
                'consumo_litros'
            )
        }),
        ('Archivos', {
            'fields': (
                'imagen',
                'fecha_registro'
            )
        })
    )
