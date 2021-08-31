from rest_framework import generics
from apps.processos.models import Processo
from .serializers import ProcessoSerializer


class ProcessoAPIView(generics.ListAPIView):
    """
    Lista todos os processos cadastrados no sistema
    """
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer