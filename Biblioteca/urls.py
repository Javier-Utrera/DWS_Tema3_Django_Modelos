from django.urls import path
from . import views

urlpatterns = [
    #el primer parametro de path le indicamos la ruta
    path('', views.index, name='index'),
    path('libros', views.listar_libros, name='url_listar_libros'),
    path('libro/<int:id_libro>',views.dame_libro, name='url_dame_libro'),
    path('libros/listar/<int:anio_libro>/<int:mes_libro>',views.dame_libro_fechas, name='url_dame_fecha'),
    #path('libros/listar/<str:idioma>',views.dame_libro_idioma, name='url_dame_idioma')
]