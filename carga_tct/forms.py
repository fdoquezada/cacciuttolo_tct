from django import forms
from .models import RegistroCombustible

class RegistroCombustibleForm(forms.ModelForm):
    class Meta:
        model = RegistroCombustible
        fields = ['fecha', 'guia', 'patente', 'estacion_servicio', 'suministro', 'kilometraje', 'consumo_litros', 'imagen']
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.usuario = self.initial.get('usuario')
        if commit:
            instance.save()
        return instance

    class Meta:
        model = RegistroCombustible
        fields = ['fecha', 'guia', 'patente', 'estacion_servicio', 'suministro', 'kilometraje', 'consumo_litros', 'imagen']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'guia': forms.TextInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'estacion_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'suministro': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'consumo_litros': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'fecha': 'Fecha',
            'guia': 'Guía',
            'patente': 'Patente',
            'estacion_servicio': 'Estación de Servicio',
            'suministro': 'Suministro',
            'kilometraje': 'Kilometraje',
            'consumo_litros': 'Consumo (Lt)',
            'imagen': 'Imagen',
        }