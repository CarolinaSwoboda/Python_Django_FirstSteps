from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True) #esto permite que sea opcional, es decir, acepta nulos y datos en blancos

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
