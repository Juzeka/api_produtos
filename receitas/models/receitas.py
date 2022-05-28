from django.db import models


class Receita(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Nome'
    )
    descriacao = models.TextField(
        blank=False,
        null=False,
        verbose_name='Descrição'
    )
    ingredientes = models.ManyToManyField(
        'ingredientes.Ingrediente',
        verbose_name='Ingredientes',
        related_name='receita_ingredientes'
    )
    etapas = models.ManyToManyField(
        'etapas.Etapa',
        verbose_name='Etapas',
        related_name='receita_etapas'
    )

    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'