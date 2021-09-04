from rest_framework import viewsets
from apps.processos.models import Processo
from apps.orgaos.models import Orgao
from apps.assuntos.models import Assunto
from apps.tramitacoes.models import Tramite
from django.contrib.auth import get_user_model
from .serializers import (ProcessoSerializer,
                          AssuntoSerializer,
                          OrgaoSerializer,
                          UserSerializer,
                          TramiteSerializer,)

User = get_user_model()


class ProcessoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os processos cadastrados no sistema
    """
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer


class OrgaoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os órgãos cadastrados no sistema
    """
    queryset = Orgao.objects.all()
    serializer_class = OrgaoSerializer


class AssuntoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os assuntos cadastrados no sistema
    """
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer


class UserAPIView(viewsets.ModelViewSet):
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
