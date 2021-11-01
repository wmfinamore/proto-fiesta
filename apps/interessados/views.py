from django.http import HttpResponse
from .models import Interessado
import json
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Cria uma função para retornar um json com os dados que queremos expor
@login_required # Decorator para verificar se o usuário está logado
def interessadosapi(request):
    if not request.user.has_perm('interessados.view_interessado'):
        # verificar se o usuário logado tem permissão para visualizar interessados
        return HttpResponse('Você não tem permissão para listar Interessados')

    interessados = Interessado.objects.all() # retorna um queryset
    list = [] # criar uma lista para receber os valores do queryset
    for interessado in interessados: # itera o queryset para recuperar o valor cada instância retornada no queryset
        valor = {} # criar um dicionário para
        valor['id'] = str(interessado.id)
        valor['nome'] = interessado.nome
        valor['nome_social'] = interessado.nome_social
        valor['cpf'] = interessado.cpf
        valor['cnpj'] = interessado.cnpj
        list.append(valor)

    data = json.dumps(list) # converte a lista em uma string no formato json
    return HttpResponse(data) # retorna o json


class InteressadosListView(LoginRequiredMixin,
                           PermissionRequiredMixin,
                           ListView,):
    model = Interessado
    context_object_name = 'interessados'
    permission_required = ('interessados.view_interessado', ) # sintaxe das permissões no Django: <nome_app>.<action>_<model>
    permission_denied_message = "Você não tem permissão para listar Interessados"


class InteressadoCreateView(
                            LoginRequiredMixin,
                            PermissionRequiredMixin,
                            CreateView,):
    model = Interessado
    context_object_name = 'interessado'
    fields = ['nome', 'nome_social', 'cpf', 'cnpj']
    success_url = '/interessados/'
    permission_required = ('interessados.add_interessado', )
    permission_denied_message = "Você não tem permissão para visualizar Interessados"


class InteressadoUpdateView(LoginRequiredMixin,
                            PermissionRequiredMixin,
                            UpdateView,):
    model = Interessado
    context_object_name = 'interessado'
    fields = ['nome', 'nome_social', 'cpf', 'cnpj']
    success_url = '/interessados/'
    permission_required = ('interessados.change_interessado',)
    permission_denied_message = "Você não tem permissão para atualizar Interessados"


class InteressadoDeleteView(LoginRequiredMixin,
                            PermissionRequiredMixin,
                            DeleteView,):
    model = Interessado
    context_object_name = 'interessado'
    success_url = reverse_lazy('interessados_lista')
    permission_required = ('interessados.delete_interessado',)
    permission_denied_message = "Você não tem permissão para excluir Interessados"
