from django.shortcuts import render, redirect
from .forms import ResenaForm
from .models import Libro, Usuario, Reseña 

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libreria/listar_libros.html', {'libros': libros})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'libreria/listar_usuarios.html', {'usuarios': usuarios})

def listar_resenas(request):
    resenas = Reseña.objects.all()
    return render(request, 'libreria/listar_resenas.html', {'resenas': resenas})

def crear_resena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.usuario = request.user
            reseña.save()
            return redirect('listar_resenas')
    else:
        form = ResenaForm()

    return render(request, 'libreria/crear_resena.html', {'form': form})