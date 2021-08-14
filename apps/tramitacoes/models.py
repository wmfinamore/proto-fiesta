from django.db import models
from apps.processos.models import Processo
from django.contrib.auth import get_user_model
from apps.orgaos.models import Orgao
import uuid
from django.urls import reverse

Usuario = get_user_model()


class Tramite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    processo = models.ForeignKey(Processo, on_delete=models.PROTECT, related_name='processo_tramites')
    orgao_destino = models.ForeignKey(Orgao, on_delete=models.PROTECT, related_name='orgao_tramites')
    despacho = models.TextField(null=True, blank=True)
    data_tramite = models.DateTimeField(auto_now_add=True)
    usuario_tramite = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='usuario_tramites')
    data_recebimento = models.DateTimeField(null=True, blank=True)
    usuario_recepcao = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True, related_name='usuario_recepcoes')

    def __str__(self):
        return str(self.processo.numero_processo) + '-' + str(self.orgao_destino.nome)

    # override da função get_absolute_url passando parâmetro para renderizar o processo que foi tramitado
    def get_absolute_url(self):
        return reverse('processo_editar', args=[self.processo.id])

    class Meta:
        ordering = ['-data_tramite']
