Instalar entorno Virtual

pip install virtualenv

c:\>python -m venv c:\path\to\myenv

ruta.\myenv\Scripts\activate


CREAR PROYECTO
django-admin startproject mysite

correr en un servidor

python manage.py runserver



para la bd (ya sea la por default o cualquiera q este conectada correctamente)

python manage.py makemigrations


python manage.py migrate
Para ejecutar las migraciones, los mensajes son q estan creando las tablas dentro de la BD


------------}
en settings se pone en installed app
el nombre del app

enn la terminal colocamos para ver los nuevoss modelos creados
python manage.py makemigrations myapp
python manage.py migrate myapp


------------importar los modelos en myapp
python manage.py shell

from myapp.models import Project, Task
p = Project(name="aplicacion movil")
p.save() 
Project.objects.all()

Project.objects.get(id=1)
Project.objects.get(name="aplicacion movil")


p = Project.objects
p.filter(name__startswith="abc")

Project.objects.get(id=1)

python manage.py createsuperuser
