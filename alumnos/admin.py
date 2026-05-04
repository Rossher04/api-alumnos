from django.contrib import admin

from .models import Alumno, Asignacion, Curso


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("alumno_id", "nombre", "apellido", "edad", "correo", "telefono")
    search_fields = ("nombre", "apellido", "correo")


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("curso_id", "nombre", "activo", "fecha_mod")
    search_fields = ("nombre",)
    list_filter = ("activo",)


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ("asignacion_id", "alumno", "curso", "activo", "fecha_mod")
    search_fields = ("alumno__nombre", "alumno__apellido", "curso__nombre")
    list_filter = ("activo",)
