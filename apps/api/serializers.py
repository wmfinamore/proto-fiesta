from rest_framework import serializers
from apps.processos.models import Processo
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
from apps.orgaos.models import Orgao


# Classe implementada para incluir Nested Relationships
class AssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assunto
        fields = ['id', 'nome', 'situacao', 'level']


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class OrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgao
        fields = ['id', 'nome', 'sigla', 'tipo', 'situacao']


# Classe que converte os dados para JSON
class ProcessoSerializer(serializers.ModelSerializer):
    assunto = AssuntoSerializer(many=False, read_only=True)
    usuario_criacao = UserSerializer(many=False, read_only=True)
    usuario_alteracao = UserSerializer(many=False, read_only=True)

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
