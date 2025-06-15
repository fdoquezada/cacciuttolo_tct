from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        
        try:
            # Enviar email al administrador
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            # Enviar confirmación al remitente
            send_mail(
                'Gracias por contactarnos',
                'Hemos recibido tu mensaje. Nos pondremos en contacto contigo pronto.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Mensaje enviado exitosamente. Te contactaremos pronto.')
            return redirect('contacto:contacto')
            
        except Exception as e:
            messages.error(request, 'Hubo un error al enviar el mensaje. Por favor, intenta nuevamente.')
            
    return render(request, 'contacto/contacto.html')
