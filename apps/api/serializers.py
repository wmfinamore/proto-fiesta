from rest_framework import serializers
from apps.processos.models import Processo


# Classe que converte os dados para JSON
class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = ('id',
                  'numero_processo',
                  'interessado',
                  'assunto',
                  'resumo',
                  'situacao',
                  'data_criacao',
                  'data_atualizacao',
                  'usuario_criacao',
                  'usuario_alteracao',
                  'unidade_atual',)
