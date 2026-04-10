from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100, default="Informatica de Gestao")
    ano_inicio = models.IntegerField(default=2024)
    ano_previsto_fim = models.IntegerField(default=2027)
    instituicao = models.CharField(max_length=100, default="Universidade Lusófona")

    def __str__(self):
        return self.nome
