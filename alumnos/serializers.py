from rest_framework import serializers

from .models import Alumno, Asignacion, Curso


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class AsignacionSerializer(serializers.ModelSerializer):
    alumno_detalle = AlumnoSerializer(source="alumno", read_only=True)
    curso_detalle = CursoSerializer(source="curso", read_only=True)

    class Meta:
        model = Asignacion
        fields = "__all__"
