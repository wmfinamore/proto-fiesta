from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


# Tipo de unidade administrativa
TIPO_UNIDADE = [
    ('F', 'Formal'),
    ('I', 'Informal')
]

# Situação da unidade administrativa
SITUACAO_UNIDADE = [
    ('A', 'Ativa'),
    ('I', 'Inativa')
]


class Orgao(MPTTModel):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    tipo = models.CharField(max_length=2, choices=TIPO_UNIDADE, default='F')
    situacao = models.CharField(max_length=2, choices=SITUACAO_UNIDADE, default='A')

    class MPTTMeta:
        order_insertion_by = ['nome']

    def get_absolute_url(self):
        return reverse('orgaos_lista')

    def __str__(self):
        return self.nome
