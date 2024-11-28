# libreria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_libros, name='listar_libros'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('resenas/', views.listar_resenas, name='listar_resenas'),
    path('crear_resena/', views.crear_resena, name='crear_resena'),
]