from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                 )
from .models import Assunto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AssuntosListView(ListView):
    model = Assunto
    context_object_name = 'assuntos'


class AssuntoCreateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        CreateView):
    permission_required = ('assuntos.add_assunto')
    permission_denied_message = "Você não tem permissão para adicionar assuntos"
    model = Assunto
    fields = ['nome', 'parent', 'situacao']
    success_url = '/assuntos/'
    success_message = 'Assuntos criado com sucesso!'


class AssuntoEditView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      UpdateView):
    permission_required = ('assuntos.change_assunto')
    permission_denied_message = "Você não tem permissão para alterar assuntos"
    model = Assunto
    fields = ['nome', 'parent', 'situacao']
    context_object_name = 'assunto'


class AssuntoDeleteView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        DeleteView):
    permission_required = ('assuntos.delete_assunto')
    permission_denied_message = "Você não tem permissão para excluir assuntos"
    model = Assunto
    context_object_name = 'assunto'
    success_url = reverse_lazy('assuntos_lista')
