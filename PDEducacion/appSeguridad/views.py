from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from appSeguridad.models import (
    Aplicacion,
    Permiso,
    Rol
)
from appSeguridad.serializers import (
    AplicacionSerializer,
    PermisoSerializer,
    RolSerializer
)

class AplicacionViewSet(viewsets.ModelViewSet):
    serializer_class = AplicacionSerializer
    queryset = Aplicacion.objects.all()

class PermisoViewSet(viewsets.ModelViewSet):
    serializer_class = PermisoSerializer
    queryset = Permiso.objects.all()

class RolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
