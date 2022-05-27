from django.db import models


class Ingrediente(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Nome'
    )
    quantidade = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Quantidade'
    )

    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
