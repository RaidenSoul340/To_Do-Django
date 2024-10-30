from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=256)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Funcionarios(models.Model):
    Nome = models.CharField(max_length=80)
    funcao = models.TextField(blank=True, null=True)
    presente = models.BooleanField(default=False)
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NomeF