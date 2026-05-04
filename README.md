# API Alumnos

API REST en Django y Django REST Framework basada en las tablas del PDF
`Hoja de Trabajo API.pdf`.

## Tablas

- Alumno: nombre, apellido, edad, genero, correo, telefono, fecha_mod.
- Curso: nombre, descripcion, fecha_mod, activo.
- Asignacion: comentarios, fecha_mod, activo, alumno, curso.

## Instalacion

```powershell
py -m venv myenv
.\myenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Rutas

- `GET/POST /api/alumnos/`
- `GET/PUT/PATCH/DELETE /api/alumnos/<id>/`
- `GET/POST /api/cursos/`
- `GET/PUT/PATCH/DELETE /api/cursos/<id>/`
- `GET/POST /api/asignaciones/`
- `GET/PUT/PATCH/DELETE /api/asignaciones/<id>/`

## Publicacion en hosting con Render

El proyecto ya incluye los archivos necesarios para Render:

- `build.sh`: instala dependencias, ejecuta `collectstatic` y aplica migraciones.
- `render.yaml`: define el servicio web y una base PostgreSQL.
- `requirements.txt`: incluye Django REST Framework, Gunicorn, WhiteNoise y PostgreSQL.

Pasos generales:

1. Subir este proyecto a GitHub.
2. Entrar a Render y crear un `Blueprint` desde el repositorio.
3. Render detectara `render.yaml` y publicara la API.
4. Al terminar, la API quedara en una URL parecida a:

```text
https://api-alumnos.onrender.com/api/alumnos/
```

Tambien se puede crear manualmente como `Web Service`:

- Build Command: `bash ./build.sh`
- Start Command: `python -m gunicorn api_alumnos.wsgi:application`
- Variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=.onrender.com`.
