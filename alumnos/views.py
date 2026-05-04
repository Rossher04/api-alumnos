from rest_framework import generics

from .models import Alumno, Asignacion, Curso
from .serializers import AlumnoSerializer, AsignacionSerializer, CursoSerializer


class ListaAlumnos(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


class AlumnoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer


class ListaCursos(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ListaAsignaciones(generics.ListCreateAPIView):
    queryset = Asignacion.objects.select_related("alumno", "curso").all()
    serializer_class = AsignacionSerializer


class AsignacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asignacion.objects.select_related("alumno", "curso").all()
    serializer_class = AsignacionSerializer
