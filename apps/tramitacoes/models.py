from django.db import models
from apps.processos.models import Processo
from django.contrib.auth import get_user_model
from apps.orgaos.models import Orgao
import uuid
from django.urls import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from simple_history.models import HistoricalRecords

Usuario = get_user_model()


class Tramite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    processo = models.ForeignKey(Processo, on_delete=models.PROTECT, related_name='processo_tramites')
    orgao_destino = models.ForeignKey(Orgao, on_delete=models.PROTECT, related_name='orgao_tramites')
    despacho = models.TextField(null=True, blank=True)
    data_tramite = models.DateTimeField(auto_now_add=True)
    usuario_tramite = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='usuario_tramites')
    data_recebimento = models.DateTimeField(null=True, blank=True)
    usuario_recepcao = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True,
                                         related_name='usuario_recepcoes')
    history = HistoricalRecords()

    def __str__(self):
        return str(self.processo.numero_processo) + '-' + str(self.orgao_destino.nome)

    # override da função get_absolute_url passando parâmetro para renderizar o processo que foi tramitado
    def get_absolute_url(self):
        return reverse('processo_editar', args=[self.processo.id])

    class Meta:
        ordering = ['-data_tramite']


# signal que atualiza a unidade atual do processo depois que uma tramitação for salva
@receiver(post_save, sender=Tramite)
def update_unidade_atual(sender, instance, created, **kwargs):
    processo = Processo.objects.get(id=instance.processo.id)
    processo.unidade_atual = instance.orgao_destino.nome
    processo.save()


# signal que atualiza a unidade atual do processo depois que uma tramitação for excluída
@receiver(post_delete, sender=Tramite)
def update_unidade_atual(sender, instance, **kwargs):
    processo = Processo.objects.get(id=instance.processo.id)
    processo.unidade_atual = processo.ultimo_tramite
    processo.save()
