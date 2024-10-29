from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=256)
    descricao = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
