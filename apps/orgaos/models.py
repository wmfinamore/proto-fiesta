import uuid
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    tipo = models.CharField(max_length=2, choices=TIPO_UNIDADE, default='F')
    situacao = models.CharField(max_length=2, choices=SITUACAO_UNIDADE, default='A')

    class MPTTMeta:
        order_insertion_by = ['nome']

    def __str__(self):
        return self.nome
