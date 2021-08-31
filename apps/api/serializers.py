from rest_framework import serializers
from apps.processos.models import Processo
from apps.assuntos.models import Assunto


# Classe implementada para incluir Nested Relationships
class AssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assunto
        fields = ['id', 'nome', 'situacao', 'level']


# Classe que converte os dados para JSON
class ProcessoSerializer(serializers.ModelSerializer):
    assunto = AssuntoSerializer(many=False, read_only=True)

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
