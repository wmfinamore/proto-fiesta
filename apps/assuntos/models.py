from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


# Situação do Assunto
SITUACAO_UNIDADE = [
    ('A', 'Ativa'),
    ('I', 'Inativa')
]


class Assunto(MPTTModel):
    nome = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    situacao = models.CharField(max_length=2, choices=SITUACAO_UNIDADE, default='A')

    def get_absolute_url(self):
        return reverse('assuntos_lista')

    def __str__(self):
        return self.nome
