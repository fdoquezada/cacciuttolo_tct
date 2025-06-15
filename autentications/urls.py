from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . import views

app_name = 'autentications'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='autentications/logged_out.html'
    ), name='logout'),
    path('register/', CreateView.as_view(
        template_name='autentications/register.html',
        form_class=UserCreationForm,
        success_url='/accounts/login/?registered=true'
    ), name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help, name='help'),
]