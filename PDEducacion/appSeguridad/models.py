from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Aplicacion(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Permiso(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    aplicacion = models.ForeignKey(
        Aplicacion,
        on_delete = models.CASCADE
    )
    permiso = models.ForeignKey(
        Permiso,
        on_delete = models.CASCADE
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add = True
    )
    fecha_actualizacion= models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.nombre
