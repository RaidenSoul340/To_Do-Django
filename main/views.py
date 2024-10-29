from django.shortcuts import render, redirect
from .models import Task

#Exibir informações no front
def task_list(request):
    tasks = Task.objects.all() #Buscando todo os dados quem tem na tabela

    return render(request, 'tasks/task_list.html', {'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        if titulo:
            Task.objects.create(titulo=titulo)
        return redirect('lista_tarefas')
    return render(request, 'tasks/add_task.html')

def delete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
