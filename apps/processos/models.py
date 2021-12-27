from django.db import models
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
from apps.interessados.models import Interessado
import uuid
from datetime import date
from django.urls import reverse
from simple_history.models import HistoricalRecords
from tinymce.models import HTMLField


# Situação do Processo
SITUACAO_UNIDADE = [
    ('A', 'Ativo'),
    ('E', 'Encerrado')
]

Usuario = get_user_model()


def interessado_processo_path(instance, filename):
    # arquivo será carregado para MEDIA_ROOT/processo_<interessado>/<filename>
    return 'p_{0}_{1}/{2}'.format(str(instance.num_processo), str(instance.data_criacao.strftime("%Y")), filename)


class Processo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num_processo = models.PositiveBigIntegerField(
        unique_for_year=date.today().strftime("%Y"), editable=False, default=0)
    interessado = models.ForeignKey(Interessado, on_delete=models.PROTECT, null=True, blank=True, related_name='processos_interessado')
    assunto = models.ForeignKey(Assunto, on_delete=models.PROTECT, related_name='processos_assunto')
    resumo = HTMLField(null=True, blank=True)
    anexo = models.FileField(null=True, blank=True, upload_to=interessado_processo_path)
    situacao = models.CharField(max_length=2, choices=SITUACAO_UNIDADE, default='A')
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False)
    data_atualizacao = models.DateTimeField(auto_now=True, editable=False)
    usuario_criacao = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='processos_usuario')
    usuario_alteracao = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name='processos_alterados', null=True, blank=True)
    unidade_atual = models.CharField(max_length=100, null=True, blank=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        # verifica se estamos inserindo um novo processo(=0) ou se é uma atualização(>0)
        if self.num_processo > 0:
            # Se for uma atualização apenas atualiza o objeto .save
            pass
        # Caso seja um novo processo, executa o procedimento para auto-incremento
        else:
            # Tenta recuperar o último processo criado no ano corrente
            processo = Processo.objects.filter(data_criacao__year=date.today().strftime("%Y"))\
                .order_by('-num_processo')\
                .first()
            # caso tenha um processo criado no ano, usa o número do processo para incrementar a numeração do novo
            # processo
            if processo:
                self.num_processo = int(processo.num_processo) + 1
            else:
                # Caso seja o primeiro processo do ano atribui o número 1
                self.num_processo = 1
                # salvamos o objeto com o método .save da superclasse
        super().save(*args, **kwargs)

    @property
    def numero_processo(self):
        ano = self.data_criacao.strftime("%Y")
        numero = self.num_processo
        return f'{numero:06}' + '/' + str(ano)

    @property
    def ultimo_tramite(self):
        # Usando select_related para otimizar a consulta do banco de dados
        tramite = self.processo_tramites.select_related('orgao_destino').first()
        if tramite:
            return tramite.orgao_destino.nome
        else:
            return 'Não tramitado'

    @property
    def recepcao(self):
        tramite_recepcao = self.processo_tramites.first()
        if tramite_recepcao:
            return tramite_recepcao.data_recebimento
        else:
            return '-'

    def get_absolute_url(self):
        return reverse('processos_lista')

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.numero_processo
