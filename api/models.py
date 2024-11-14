from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=120)
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    contato = models.CharField(max_length=120)
    tipo = models.CharField(max_length=40)
    descricao = models.CharField(max_length=120)
