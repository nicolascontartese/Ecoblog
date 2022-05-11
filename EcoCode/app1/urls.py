from re import template
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from app1 import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), 
    path('nosotros', views.nosotros, name="Nosotros"),
    path('Blog', views.blog, name="Blog"),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='app1/logout.html'), name="logout"),
    path('error', LogoutView.as_view(template_name='app1/error.html'), name="error"),
    path('correcto', LogoutView.as_view(template_name='app1/correcto.html'), name="correcto"),


    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    

    
]