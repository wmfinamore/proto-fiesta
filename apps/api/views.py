from rest_framework import viewsets
from apps.processos.models import Processo
from .serializers import ProcessoSerializer, AssuntoSerializer, Orgao, UserSerializer


class ProcessoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os processos cadastrados no sistema
    """
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer


class Assunto