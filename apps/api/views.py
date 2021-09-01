from rest_framework import viewsets
from apps.processos.models import Processo
from apps.orgaos.models import Orgao
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model
from .serializers import ProcessoSerializer, AssuntoSerializer, OrgaoSerializer, UserSerializer

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