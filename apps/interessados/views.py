from django.http import HttpResponse
from .models import Interessado
import json
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Cria uma função para retornar um json com os dados que queremos expor
def interessadosapi(request):
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


class InteressadosListView(ListView):
    model = Interessado
    context_object_name = 'interessados'


class InteressadoCreateView(CreateView):
    model = Interessado
    context_object_name = 'interessado'
    fields = ['nome', 'nome_social', 'cpf', 'cnpj']
    success_url = '/interessados/'


class InteressadoUpdateView(UpdateView):
    model = Interessado
    context_object_name = 'interessado'
    fields = ['nome', 'nome_social', 'cpf', 'cnpj']
    success_url = '/interessados/'


class InteressadoDeleteView(DeleteView):
    model = Interessado
    context_object_name = 'interessado'
    success_url = reverse_lazy('interessados_lista')
