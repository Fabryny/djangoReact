from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=50)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
