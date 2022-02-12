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
                          InteressadoSerializer,
                          CargoSerializer,)
from apps.interessados.models import Interessado
from apps.cargos.models import Cargo


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

    def get_queryset(self):
        # Sobrescrever o métodos get_queryset para filtrar a chamada ajax do
        # formulário de trâmites ou outros que busquem órgãos pelo nome
        # if self.request.is_ajax():
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            term = self.request.GET.get('term')
            orgaos = Orgao.objects.filter(nome__icontains=term)
            return orgaos
        return Orgao.objects.all()


class AssuntoAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Lista todos os assuntos cadastrados no sistema
    """
    queryset = Assunto.objects.all()
    serializer_class = AssuntoSerializer

    def get_queryset(self):
        # Sobrescrever o métodos get_queryset para filtrar a chamada ajax do
        # formulário de processos ou outros que busquem interessados pelo nome
        # if self.request.is_ajax():
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            term = self.request.GET.get('term')
            assuntos = Assunto.objects.filter(nome__icontains=term)
            return assuntos
        return Assunto.objects.all()


class UserAPIView(viewsets.ReadOnlyModelViewSet):
    """
    Lista todos os usuários cadastrados no sistema
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # Sobrescrever o métodos get_queryset para filtrar a chamada ajax do
        # formulário de processos ou outros que busquem interessados pelo nome
        # if self.request.is_ajax():
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            term = self.request.GET.get('term')
            user = User.objects.filter(first_name__icontains=term)
            return user
        return User.objects.all()


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

    def get_queryset(self):
        # Sobrescrever o métodos get_queryset para filtrar a chamada ajax do
        # formulário de processos ou outros que busquem interessados pelo nome
        # if self.request.is_ajax():
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            term = self.request.GET.get('term')
            interessados = Interessado.objects.filter(nome__icontains=term)
            return interessados
        return Interessado.objects.all()


class CargoAPIView(viewsets.ModelViewSet):
    """API para o app Cargos, model Cargo"""
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        # Sobrescrever o métodos get_queryset para filtrar a chamada ajax do
        # formulário de processos ou outros que busquem cargos pelo nome
        # if self.request.is_ajax():
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            term = self.request.GET.get('term')
            cargos = Cargo.objects.filter(nome__icontains=term)
            return cargos
        return Cargo.objects.all()
