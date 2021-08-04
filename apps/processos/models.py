from django.db import models
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
import uuid

# Situação do Processo
SITUACAO_UNIDADE = [
    ('A', 'Ativo'),
    ('E', 'Encerrado')
]

Usuario = get_user_model()


class Processo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num_processo = models.PositiveBigIntegerField(unique_for_year=True, editable=False)
    interessado = models.CharField(max_length=200)
    assunto = models.ForeignKey(Assunto, on_delete=models.PROTECT, related_name='processos_assunto')
    resumo = models.TextField(null=True, blank=True)
    situacao = models.CharField(max_length=2, choices=SITUACAO_UNIDADE, default='A')
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False)
    data_atualizacao = models.DateTimeField(auto_now=True, editable=False)
    usuario_criacao = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='processos_usuario')
    usuario_alteracao = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name='processos_alterados', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        ano = self.data_criacao.strftime("%Y")
        return str(self.num_processo) + '/' + str(ano)
