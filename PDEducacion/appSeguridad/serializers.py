from rest_framework import serializers

from appSeguridad.models import (
    Aplicacion,
    Permiso,
    Rol
)

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacion
        fields = ('id', 'nombre')

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('id','nombre')

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('id','nombre', 'aplicacion', 'permiso')
