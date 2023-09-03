from django.shortcuts import render, redirect # Importar el módulo render de Django, que nos permite renderizar un archivo html y el módulo redirect de Django, que nos permite redireccionar a otra vista o url
from django.http import HttpResponse, JsonResponse # Importar el módulo HttpResponse de Django
from .models import Project, Task # Importar el modelo Project
from django.shortcuts import get_object_or_404 # Importar el módulo get_object_or_404 de Django
from .forms import CreateNewTask, CreateNewProject # Importar el formulario CreateNewTask de Django

# Utilities
from datetime import datetime

# Create your views here.
# Aquí se va a definir lo que queramos enviar a la pantalla, como archivos html, variables, etc. Se pueden añadir más vistas aquí

def index(request):
    title = 'Django Course!! {now}'.format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
    return render(request, 'index.html',{
        'title': title
        })

def about(request):
    username = 'User'
    return render(request, 'about.html',{
        'username': username
    })

# Función que devuelve un saludo
def hello(request, username):
    print("imprimir:")
    print(request)
    return HttpResponse("<h2>hello %s</h2>"% username)

def projects(request):
    #projects = list(Project.objects.values()) # Obtener todos los proyectos de la base de datos 
    projects = Project.objects.all() # Obtener todos los proyectos de la base de datos
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def tasks(request):
    #task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all() # Obtener todas las tareas de la base de datos
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

def createTask(request):
    if request.method == 'GET':
        #Show interfaz
        return render(request, 'tasks/create_task.html',{
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            project_id = 2
        )
        return redirect('tasks')

def createProject(request):
    if request.method == 'GET':
        #Show interfaz
        return render(request, 'projects/create_project.html',{
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(
            name = request.POST['name'],
        )
        return redirect('projects')

def projectDetail(request, id):
    project = get_object_or_404(Project, id=id)
    #tasks = Task.objects.all() # Obtener todas las tareas de la base de datos
    tasks = Task.objects.filter(project_id=id) # Obtener todas las tareas de la base de datos que pertenecen al proyecto con id = id
    return render(request, 'projects/project_detail.html',{
        'project': project,
        'tasks': tasks
    })

#def projects(request):
    #projects = list(Project.objects.values()) # Obtener todos los proyectos de la base de datos 
    #return JsonResponse(projects, safe=False)

#def tasks(request, title):
    #task = get_object_or_404(Task, title=title)
    #return HttpResponse('task %s' %task.title)

def hi(request):
    '''Hi.'''
    #return HttpResponse("prueba")
    numbers = request.GET['numbers']
    numbers = list(numbers.split(","))
    orderMin(numbers)
    return HttpResponse(str(numbers))

def orderMin(numbers = []):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                aux = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = aux