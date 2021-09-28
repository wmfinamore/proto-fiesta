from rest_framework import viewsets, permissions, generics
from apps.processos.models import Processo
from apps.orgaos.models import Orgao
from apps.assuntos.models import Assunto
from apps.tramitacoes.models import Tramite
from django.contrib.auth import get_user_model
from apps.cargos.models import Vinculo
from .serializers import (ProcessoSerializer,
                          AssuntoSerializer,
                          OrgaoSerializer,
                          UserSerializer,
                          TramiteSerializer,
                          InteressadoSerializer,)
from apps.interessados.models import Interessado


User = get_user_model()


class ProcessoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os processos cadastrados no sistema
    """
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]


class OrgaoAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Lista todos os órgãos cadastrados no sistema
    """
    queryset = Orgao.objects.all()
    serializer_class = OrgaoSerializer


class AssuntoAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Lista todos os assuntos cadastrados no sistema
    """
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer


class UserAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Lista todos os usuários cadastrados no sistema
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TramiteAPIView(viewsets.ModelViewSet):
    """
    Lista todos os tramites realizados no sistema
    """
    queryset = Tramite.objects.all()
    serializer_class = TramiteSerializer
    filter_fields = ['processo']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class CaixaPostalAPIView(generics.ListAPIView):
    serializer_class = ProcessoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        # seleciona os vínculos do usuário que fez o request
        vinculos = Vinculo.objects.filter(funcionario=self.request.user)
        data = []
        # Criar lista para usar os dados no filtro da "caixa postal"
        for unidade in vinculos:
            data.append(unidade.lotacao.nome)
        """
            retorna os processos cujo nome do último trâmite é igual as unidades
            de lotação do usuário que fez o request
        """
        return Processo.objects.filter(unidade_atual__in=data)


class InteressadoAPIView(viewsets.ModelViewSet):
    """API para o app Interessados"""
    queryset = Interessado.objects.all()
    serializer_class = InteressadoSerializer
    permission_classes = [permissions.IsAuthenticated, ]
