from rest_framework import serializers
from apps.processos.models import Processo
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
from apps.orgaos.models import Orgao


class ParentAssuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assunto
        fields = ['nome']


class AssuntoSerializer(serializers.ModelSerializer):
    parent = ParentAssuntoSerializer(many=False, read_only=True)

    class Meta:
        model = Assunto
        fields = ['id', 'nome', 'situacao', 'level', 'parent']


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ParentOrgaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgao
        fields = ['nome']


class OrgaoSerializer(serializers.ModelSerializer):
    parent = ParentOrgaoSerializer(many=False, read_only=True)

    class Meta:
        model = Orgao
        fields = ['id', 'nome', 'sigla', 'tipo', 'situacao', 'level', 'parent']


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
