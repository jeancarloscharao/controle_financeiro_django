from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class StatusContaReceber(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Status"
        verbose_name = "Status"
        ordering = ['nome']


class ContaReceber(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField(null=False, blank=False)
    emissao = models.DateTimeField(default=datetime.now, blank=True)
    data_receber = models.DateTimeField(default=datetime.now, blank=True)
    status = models.ForeignKey(StatusContaReceber, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Contas à Receber"
        verbose_name = "Conta à Receber"
        ordering = ['id']
