from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from appUniversidad.models import (
    ProgramaCurricular,
    Facultad,
    ContenidoPrograma,
    Materia,
    Hora,
    Sede,
    Horario
)

@admin.register(ProgramaCurricular)
class ProgramaCurricularAdmin(ImportExportModelAdmin):
    list_display = [
        'nombre'
    ]

@admin.register(Facultad)
class FacultadAdmin(ImportExportModelAdmin):
    list_display = [
        'nombre'
    ]

@admin.register(ContenidoPrograma)
class ContenidoProgramaAdmin(ImportExportModelAdmin):
    list_display = [
        'nombre',
        'tiempo',
        'programacurricular',
        'facultad'
    ]
    list_filter = [
        'nombre',
        'tiempo',
        'programacurricular',
        'facultad'
    ]
    fields = (
        'nombre',
        'tiempo',
        'programacurricular',
        'facultad'
    )

@admin.register(Materia)
class MateriaAdmin(ImportExportModelAdmin):
    list_display = [
        'nombre',
        'contenidoprograma'
    ]

@admin.register(Hora)
class HoraAdmin(ImportExportModelAdmin):
    list_display = [
        'inicio',
        'fin',
    ]

@admin.register(Sede)
class SedeAdmin(ImportExportModelAdmin):
    list_display = [
        'nombre'
    ]

@admin.register(Horario)
class HorarioAdmin(ImportExportModelAdmin):
    list_display = [
        'materia',
        'sede',
        'hora'
    ]
