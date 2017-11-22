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
        'nombre'
    ]

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'aplicacion',
        'permiso',
        'fecha_creacion',
        'fecha_actualizacion'
    ]
    search_fields = [
        'nombre'
    ]
    list_filter = ['aplicacion','permiso']
