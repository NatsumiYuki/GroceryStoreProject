from django.db import models
from django.contrib.sessions.models import Session


class Lista(models.Model):
    session_key = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Item(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE, related_name='itens')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='itens')

    nome = models.CharField(max_length=100)
    imagem_url = models.URLField(blank=True, null=True)
    produto_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=50, default="Pendente")

    def __str__(self):
        return self.nome
