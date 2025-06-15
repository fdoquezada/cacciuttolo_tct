from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RegistroCombustible
from .forms import RegistroCombustibleForm

# Create your views here.
@login_required
def carga_tct(request):
    registros = RegistroCombustible.objects.filter(usuario=request.user).order_by('-fecha', '-fecha_registro')
    return render(request, 'carga_tct/carga_tct.html', {'registros': registros})

@login_required
def crear_registro(request):
    if request.method == 'POST':
        form = RegistroCombustibleForm(request.POST, request.FILES, initial={'usuario': request.user})
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de combustible creado exitosamente.')
            return redirect('carga_tct:carga_tct')
    else:
        form = RegistroCombustibleForm(initial={'usuario': request.user})
    
    return render(request, 'carga_tct/crear_registro.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_registro(request, registro_id):
    registro = get_object_or_404(RegistroCombustible, id=registro_id)
    
    if request.method == 'POST':
        form = RegistroCombustibleForm(request.POST, request.FILES, instance=registro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de combustible actualizado exitosamente.')
            return redirect('carga_tct:carga_tct')
    else:
        form = RegistroCombustibleForm(instance=registro)
    
    return render(request, 'carga_tct/formulario_registro.html', {'form': form, 'accion': 'Editar', 'registro': registro})

@login_required
def eliminar_registro(request, registro_id):
    registro = get_object_or_404(RegistroCombustible, id=registro_id)
    
    if request.method == 'POST':
        registro.delete()
        messages.success(request, 'Registro de combustible eliminado exitosamente.')
        return redirect('carga_tct:carga_tct')
    
    return render(request, 'carga_tct/confirmar_eliminar.html', {'registro': registro})
