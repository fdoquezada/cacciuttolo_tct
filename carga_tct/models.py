from django.db import models
from django.conf import settings
import os

# Create your models here.
def get_image_upload_path(instance, filename):
    return os.path.join('combustible_imagenes', filename)

class RegistroCombustible(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha = models.DateField(verbose_name="Fecha")
    guia = models.CharField(max_length=50, verbose_name="Guía")
    patente = models.CharField(max_length=10, verbose_name="Patente")
    estacion_servicio = models.CharField(max_length=100, verbose_name="Estación de Servicio")
    suministro = models.CharField(max_length=50, verbose_name="Suministro")
    kilometraje = models.IntegerField(verbose_name="KMS")
    consumo_litros = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Consumo [Lt]")
    imagen = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
        verbose_name="Imagen"
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Registro {self.id} - {self.fecha} - {self.patente}"
    
    class Meta:
        verbose_name = "Registro de Combustible"
        verbose_name_plural = "Registros de Combustible"
        ordering = ['-fecha', '-fecha_registro']
