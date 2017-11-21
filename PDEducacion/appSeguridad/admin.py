from django.contrib import admin

from appSeguridad.models import (
    Aplicacion,
    Permiso,
    Rol
)

@admin.register(Aplicacion)
class AplicacionAdmin(admin.ModelAdmin):
    list_display = [
        'nombre'
    ]

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'aplicacion',
        'fecha_creacion',
        'fecha_actualizacion'
    ]
    search_fields = [
        'nombre'
    ]
    list_filter = ['aplicacion']

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'permiso',
        'fecha_creacion',
        'fecha_actualizacion'
    ]
    search_fields = [
        'nombre'
    ]
    list_filter = ['permiso']
