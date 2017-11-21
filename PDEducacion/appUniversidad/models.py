from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ProgramaCurricular(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Facultad(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class ContenidoPrograma(models.Model):
    nombre = models.CharField(max_length=30)
    tiempo = models.CharField(max_length=2)
    programacurricular = models.ForeignKey(
        ProgramaCurricular,
        on_delete = models.CASCADE
    )
    facultad = models.ForeignKey(
        Facultad,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.nombre

"""class TipoCliente(models.Model):
    nombre = models.CharField(max_length=30)

class Cliente(models.Model):
    nombres = models.CharField(
        max_length = 30
    )
    apellidos = models.CharField(
        max_length = 30
    )
    cedula = models.CharField(
        max_length = 20
    )
    telefono = models.CharField(
        max_length = 30
    )
    direccion = models.CharField(
        max_length = 30
    )
    tipocliente = models.ForeignKey(
        TipoCliente,
        on_delete = models.CASCADE
    )

    def _str_(self):
        return (self.nombres + ' ' + self.apellidos)"""

class Materia(models.Model):
    nombre = models.CharField(max_length = 30)
    contenidoprograma = models.ForeignKey(
        ContenidoPrograma,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.nombre

class Hora(models.Model):
    inicio = models.CharField(max_length = 2)
    fin = models.CharField(max_length = 2)

    def __str__(self):
        return (self.inicio + ' ' + self.fin)

class Sede(models.Model):
    nombre = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    materia = models.ForeignKey(
        Materia,
        on_delete = models.CASCADE
    )
    sede = models.ForeignKey(
        Sede,
        on_delete = models.CASCADE
    )
    hora = models.ForeignKey(
        Hora,
        on_delete = models.CASCADE
    )
