from django.views.generic import (
                                    TemplateView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                 )
from .models import Orgao
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class OrgaosListView(TemplateView):
    template_name = "orgaos/orgaos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # verificar se o usuário que fez a requisição é super usuário
        # ou se tem a permissão necessária
        if self.request.user.is_superuser:
            context['orgaos'] = Orgao.objects.all()
        else:
            # senão filtra o queryset para exibir apenas os registros ativos
            context['orgaos'] = Orgao.objects.filter(situacao='A')
        return context


class OrgaoCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      CreateView,):
    permission_required = ('orgaos.add_orgao',)
    permission_denied_message = "Você não tem permissão para visualizar adicionar órgãos"
    model = Orgao
    fields = ['nome', 'sigla', 'parent', 'tipo', 'situacao', ]
    success_url = '/orgaos/'
    success_message = "Órgão foi criado com sucesso!"


class OrgaoEditView(LoginRequiredMixin,
                    PermissionRequiredMixin,
                    UpdateView):
    permission_required = ('orgaos.change_orgao',)
    permission_denied_message = "Você não tem permissão para editar órgãos"
    model = Orgao
    fields = ['nome', 'sigla', 'parent', 'tipo', 'situacao', ]
    context_object_name = 'orgao'


class OrgaoDeleteView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      DeleteView):
    permission_required = ('orgaos.delete_orgao',)
    permission_denied_message = "Você não tem permissão para excluir órgãos"
    model = Orgao
    success_url = reverse_lazy('orgaos_lista')
    context_object_name = 'orgao'