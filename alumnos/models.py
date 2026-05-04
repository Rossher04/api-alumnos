from django.db import models


class Alumno(models.Model):
    alumno_id = models.AutoField(primary_key=True, db_column="AlumnoId")
    nombre = models.CharField(max_length=100, db_column="Nombre")
    apellido = models.CharField(max_length=100, db_column="Apellido")
    edad = models.IntegerField(db_column="Edad")
    genero = models.CharField(max_length=25, db_column="Genero")
    correo = models.CharField(max_length=100, db_column="Correo")
    telefono = models.CharField(max_length=15, db_column="Telefono")
    fecha_mod = models.DateTimeField(auto_now=True, db_column="FechaMod")

    class Meta:
        db_table = "Alumno"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True, db_column="CursoId")
    nombre = models.CharField(max_length=100, db_column="Nombre")
    descripcion = models.CharField(max_length=300, db_column="Descripcion")
    fecha_mod = models.DateTimeField(auto_now=True, db_column="FechaMod")
    activo = models.BooleanField(default=True, db_column="Activo")

    class Meta:
        db_table = "Curso"

    def __str__(self):
        return self.nombre


class Asignacion(models.Model):
    asignacion_id = models.AutoField(primary_key=True, db_column="AsignacionId")
    comentarios = models.CharField(max_length=300, db_column="Comentarios")
    fecha_mod = models.DateTimeField(auto_now=True, db_column="FechaMod")
    activo = models.BooleanField(default=True, db_column="Activo")
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name="asignaciones",
        db_column="AlumnoId",
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="asignaciones",
        db_column="CursoId",
    )

    class Meta:
        db_table = "Asignacion"

    def __str__(self):
        return f"Asignacion de {self.alumno} a {self.curso}"
