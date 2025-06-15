from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from carga_tct.models import RegistroCombustible as RegistroTCT
from datetime import date


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('autentications:dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'autentications/login.html')

def logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada exitosamente para {username}!')
            return redirect('login')
        else:
            # Manejar errores específicos
            if 'username' in form.errors:
                messages.error(request, 'El nombre de usuario ya existe o no es válido')
            if 'password1' in form.errors:
                messages.error(request, 'La contraseña debe tener al menos 8 caracteres y contener letras y números')
            if 'password2' in form.errors:
                messages.error(request, 'Las contraseñas no coinciden')
            # Mostrar todos los errores del formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'autentications/register.html', {'form': form})

@login_required
def dashboard(request):
    # Obtener estadísticas solo para el usuario actual
    total_registros = RegistroTCT.objects.filter(usuario=request.user).count()
    registros_hoy = RegistroTCT.objects.filter(
        usuario=request.user,
        fecha_registro__date=date.today()
    ).count()
    registros_mes = RegistroTCT.objects.filter(
        usuario=request.user,
        fecha_registro__month=date.today().month
    ).count()
    
    context = {
        'total_registros': total_registros,
        'registros_hoy': registros_hoy,
        'registros_mes': registros_mes,
    }
    return render(request, 'autentications/dashboard.html', context)

@login_required
def settings(request):
    return render(request, 'autentications/settings.html')

@login_required
def help(request):
    return render(request, 'autentications/help.html')

# Create your views here.
