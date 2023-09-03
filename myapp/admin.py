from django.contrib import admin
from .models import Project, Task

# Register your models here.
# Crear datos de administrador, como usuarios, grupos, etc. Se pueden añadir más datos de administrador aquí

admin.site.register(Project)
admin.site.register(Task)