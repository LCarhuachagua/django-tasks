from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}), label="Descripción de Tarea")

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre de Proyecto", max_length=200)