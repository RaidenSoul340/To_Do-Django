from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='lista_tarefas'),
    path('Funcionarios/', views.ListaFuncionario, name='Lista_funcionarios'),
    path('addFuncionarios/', views.add_funcionario, name='add_funcionario'),
    path('add/', views.add_task, name='add_task'),
#    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
