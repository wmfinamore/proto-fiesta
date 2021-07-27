from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Situação da unidade administrativa
SITUACAO_UNIDADE = [
    ('A', 'Ativa'),
    ('I', 'Inativa')
]


class Assunto(MPTTModel):
    nome = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    situacao = models.CharField(max_length=2, choices=SITUACAO_UNIDADE, default='A')

    def __str__(self):
        return self.nome
