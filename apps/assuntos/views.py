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

    # override da função get_queryset set para exibir apenas registros ativos
    # para usuários sem permissão
    def get_queryset(self):
        # executa o get_queryset da classe pai
        qs = super().get_queryset()
        # verificar se o usuário que fez a requisição é super usuário
        # ou se tem a permissão necessária
        if self.request.user.is_superuser:
            return qs
        # senão filtra o queryset para exibir apenas os registros ativos
        return qs.filter(situacao='A')


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
