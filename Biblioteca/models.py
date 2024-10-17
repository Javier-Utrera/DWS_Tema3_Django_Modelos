from django.db import models
from django.conf import settings
from django.utils import timezone 

# Create your models here.
class Bilioteca(models.Model):
    direccion=models.TextField()
    
class Autor(models.Model):
    nombre= models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200,blank=True)
    edad = models.IntegerField(null=True)

class Libro(models.Model):
    IDIOMAS = [
        ("ES","Español"),
        ("EN","Ingles"),
        ("FR","Frances"),
        ("IT","Italiano"),
    ]
    
    nombre=models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES"
    )
    
    descripcion=models.TextField()
    fecha_publicacion = models.DateTimeField()
    biblioteca = models.ForeignKey(Bilioteca, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=200,unique=True)
    puntos = models.FloatField(default=5.0,db_column="puntos_biblioteca")
    libros = models.ManyToManyField(Libro, through='Prestamos',related_name="libros")
    libros_preferidos = models.ForeignKey(Libro, on_delete=models.CASCADE,related_name="favoritos")

class DatosCliente(models.Model):
    direccion= models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE)
    
    
class Prestamos(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro= models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo= models.DateTimeField(default=timezone.now)