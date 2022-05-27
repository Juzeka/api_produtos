from tabnanny import verbose
from django.db import models


class Etapa(models.Model):
    ordem = models.IntegerField(blank=False, null=False, verbose_name='Ordem')
    passo = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Passo'
    )
    descriacao = models.TextField(
        blank=False,
        null=False,
        verbose_name='Descrição'
    )

    def __str__(self):
        return self.passo


    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'
