from rest_framework import viewsets
from apps.processos.models import Processo
from apps.assuntos.models import Assunto
from .serializers import ProcessoSerializer, AssuntoSerializer, Orgao, UserSerializer


class ProcessoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os processos cadastrados no sistema
    """
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer


class AssuntoAPIView(viewsets.ModelViewSet):
    """
    Lista todos os assuntos cadastrados no sistema
    """
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer
