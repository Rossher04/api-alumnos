# Generated manually for the API Alumnos project.

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "alumno_id",
                    models.AutoField(
                        db_column="AlumnoId",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("nombre", models.CharField(db_column="Nombre", max_length=100)),
                ("apellido", models.CharField(db_column="Apellido", max_length=100)),
                ("edad", models.IntegerField(db_column="Edad")),
                ("genero", models.CharField(db_column="Genero", max_length=25)),
                ("correo", models.CharField(db_column="Correo", max_length=100)),
                ("telefono", models.CharField(db_column="Telefono", max_length=15)),
                ("fecha_mod", models.DateTimeField(auto_now=True, db_column="FechaMod")),
            ],
            options={
                "db_table": "Alumno",
            },
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "curso_id",
                    models.AutoField(
                        db_column="CursoId",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("nombre", models.CharField(db_column="Nombre", max_length=100)),
                ("descripcion", models.CharField(db_column="Descripcion", max_length=300)),
                ("fecha_mod", models.DateTimeField(auto_now=True, db_column="FechaMod")),
                ("activo", models.BooleanField(db_column="Activo", default=True)),
            ],
            options={
                "db_table": "Curso",
            },
        ),
        migrations.CreateModel(
            name="Asignacion",
            fields=[
                (
                    "asignacion_id",
                    models.AutoField(
                        db_column="AsignacionId",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("comentarios", models.CharField(db_column="Comentarios", max_length=300)),
                ("fecha_mod", models.DateTimeField(auto_now=True, db_column="FechaMod")),
                ("activo", models.BooleanField(db_column="Activo", default=True)),
                (
                    "alumno",
                    models.ForeignKey(
                        db_column="AlumnoId",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="asignaciones",
                        to="alumnos.alumno",
                    ),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        db_column="CursoId",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="asignaciones",
                        to="alumnos.curso",
                    ),
                ),
            ],
            options={
                "db_table": "Asignacion",
            },
        ),
    ]
