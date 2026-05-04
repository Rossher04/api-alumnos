from django.urls import path

from .views import (
    AlumnoDetalle,
    AsignacionDetalle,
    CursoDetalle,
    ListaAlumnos,
    ListaAsignaciones,
    ListaCursos,
)

urlpatterns = [
    path("alumnos/", ListaAlumnos.as_view(), name="lista_alumnos"),
    path("alumnos/<int:pk>/", AlumnoDetalle.as_view(), name="detalle_alumno"),
    path("cursos/", ListaCursos.as_view(), name="lista_cursos"),
    path("cursos/<int:pk>/", CursoDetalle.as_view(), name="detalle_curso"),
    path("asignaciones/", ListaAsignaciones.as_view(), name="lista_asignaciones"),
    path(
        "asignaciones/<int:pk>/",
        AsignacionDetalle.as_view(),
        name="detalle_asignacion",
    ),
]
