from django.db import models

# Create your models here.
# Crear clases de modelos, que son las tablas de la base de datos. Se pueden añadir más clases de modelos aquí

class Project(models.Model):
    name = models.CharField(max_length=200) # Campo de texto es CharField

    def __str__(self) -> str:
        return self.name

# 1 'crear web'

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() # Campo de texto largo es TextField
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Relación de uno a muchos (un proyecto tiene muchas tareas
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + '-' + self.project.name

# 1 'descargar python' 1