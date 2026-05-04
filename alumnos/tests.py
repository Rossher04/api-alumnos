from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Alumno, Asignacion, Curso


class ApiAlumnosTests(APITestCase):
    def test_crea_alumno(self):
        response = self.client.post(
            reverse("lista_alumnos"),
            {
                "nombre": "Rocio",
                "apellido": "Chaj",
                "edad": 20,
                "genero": "Femenino",
                "correo": "rocio@example.com",
                "telefono": "12345678",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alumno.objects.count(), 1)

    def test_crea_asignacion(self):
        alumno = Alumno.objects.create(
            nombre="Rocio",
            apellido="Chaj",
            edad=20,
            genero="Femenino",
            correo="rocio@example.com",
            telefono="12345678",
        )
        curso = Curso.objects.create(
            nombre="Programacion Dispositivos Moviles I",
            descripcion="Curso de desarrollo movil",
        )

        response = self.client.post(
            reverse("lista_asignaciones"),
            {
                "comentarios": "Asignacion inicial",
                "activo": True,
                "alumno": alumno.pk,
                "curso": curso.pk,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Asignacion.objects.count(), 1)
