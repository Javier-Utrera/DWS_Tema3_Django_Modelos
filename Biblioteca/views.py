from django.shortcuts import render
from .models import *
# Create your views here.
def listar_libros(request):
    libros= Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros= libros.all()
    return render(request,"libros/libros.html",{"view_libros_mostrar":libros})

def index(request):
    return render(request,"index.html")

def dame_libro(request,id_libro):
    libro=Libro.objects.select_related("biblioteca").prefetch_related("autores").get(id=id_libro)
    return render(request,"libros/unlibro.html",{"view_libro_mostrar":libro})

def dame_libro_fechas(request,anio_libro,mes_libro):
    libros=Libro.objects.select_related("biblioteca").prefetch_related("autores")
                                                      #la ',' entre los dos filtros es un AND
    libros=libros.filter(fecha_publicacion__year=anio_libro,fecha_publicacion__month=mes_libro)
    return render(request,"libros/libros.html",{"view_libros_mostrar":libros})

def dame_libro_idioma(request,idioma):
    libros=Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros=libros.filter(Q(idioma=idioma)|Q(idioma="ES")).order_by("fecha_publicacion")
    return render(request,"libros/libros.html",{"view_libros_mostrar":libros})