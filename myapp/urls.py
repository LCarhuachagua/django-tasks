from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),    
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.projectDetail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_tasks/', views.createTask, name="create_tasks"),
    path('create_projects/', views.createProject, name="create_projects"),
    path('hi/', views.hi, name="hi")
]
