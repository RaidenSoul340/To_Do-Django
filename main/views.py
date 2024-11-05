from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Funcionarios

#================================================================================#
#Exibir informações no front
@login_required #Um requerimento caso tente acessar tem quer fazer um login
def task_list(request):
    tasks = Task.objects.all() #Buscando todo os dados quem tem na tabela

    return render(request, 'tasks/task_list.html', {'tasks':tasks})

def ListaFuncionario(request):
    funcionarios_on = Funcionarios.objects.filter(presente=True)
    funcionarios_off = Funcionarios.objects.filter(presente=False)
    return render(request, 'funcionarios/funciorios_lista.html', {'funcionarios_on':funcionarios_on, 'funcionarios_off':funcionarios_off})
#================================================================================#
@login_required
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
#================================================================================#
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('lista_tarefas')

def delete_funcionario(request, funcionario_id):
    funcionario = get_object_or_404(Funcionarios, id=funcionario_id)
    funcionario.delete()
    return redirect('Lista_funcionarios')
#================================================================================#
def atualizar_tasks(request, id):
    atualizar = get_object_or_404(Task, id=id)

    if request.method == "POST":

        atualizar.titulo = request.POST.get('titulo')
        atualizar.descricao = request.POST.get('descricao')
        atualizar.status = request.POST.get('status')

        if atualizar.status:
            atualizar.status = True
        else:
            atualizar.status = False

        atualizar.save()

        return redirect('lista_tarefas')
    return render(request, 'tasks/atualizar_tarefas.html', {'tasks':atualizar})

def atualizar_funcionario(request, id):
    atualizar = get_object_or_404(Funcionarios, id=id)

    if request.method == 'POST':
        atualizar.Nome = request.POST.get('nome')
        atualizar.funcao = request.POST.get('funcao')
        atualizar.presente = request.POST.get('presente')
    
        if atualizar.presente:
            atualizar.presente = True
        else:
            atualizar.presente = False
        
        atualizar.save()
        
        return redirect('Lista_funcionarios')
    return render(request, 'funcionarios/atualizar_funcionarios.html', {'funcionario':atualizar})
#================================================================================#


