from django.db import models

# Create your models here.


class Galeria(models.Model):

    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=70)
    Imagen = models.ImageField()


class Taller(models.Model):

    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Email = models.EmailField()


class Contacto(models.Model):

    Nombre = models.CharField(max_length=30)
    Email = models.EmailField()
    Mensaje = models.CharField(max_length=100)
    




