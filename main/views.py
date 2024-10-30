from django.shortcuts import render, redirect
from .models import Task, Funcionarios

#Exibir informações no front
def task_list(request):
    tasks = Task.objects.all() #Buscando todo os dados quem tem na tabela

    return render(request, 'tasks/task_list.html', {'tasks':tasks})

def add_task(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        status = request.POST.get('status')

        if status:
            status = True
        else:
            status = False

        Task.objects.create(titulo=titulo, descricao=descricao, status=status)

        return redirect('lista_tarefas')
    return render(request, 'tasks/add_task.html')

def delete_task(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

#================================================================================#
def ListaFuncionario(request):
    funcionarios_on = Funcionarios.objects.filter(presente=True)
    funcionarios_off = Funcionarios.objects.filter(presente=False)
    return render(request, 'funcionarios/funciorios_lista.html', {'funcionarios_on':funcionarios_on, 'funcionarios_off':funcionarios_off})

def add_funcionario(request):
    if request.method == "POST":
        Nome = request.POST.get('nome')
        funcao = request.POST.get('funcao')
        presente= request.POST.get('presente')

        if presente:
            presente = True
        else:
            presente = False

        Funcionarios.objects.create(Nome=Nome, funcao=funcao, presente=presente)

        return redirect('Lista_funcionarios')
    return render(request, 'funcionarios/add_funcionarios.html')



