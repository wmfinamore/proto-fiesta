from django.views.generic import (
                                    TemplateView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                 )
from .models import Orgao
from django.urls import reverse_lazy


class OrgaosListView(TemplateView):
    template_name = "orgaos/orgaos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orgaos'] = Orgao.objects.all()
        return context


class OrgaoCreateView(CreateView):
    model = Orgao
    fields = ['nome', 'sigla', 'parent', 'tipo', 'situacao', ]
    success_url = '/orgaos/'
    success_message = "Órgão foi criado com sucesso!"


class OrgaoEditView(UpdateView):
    model = Orgao
    fields = ['nome', 'sigla', 'parent', 'tipo', 'situacao', ]
    context_object_name = 'orgao'


class OrgaoDeleteView(DeleteView):
    model = Orgao
    success_url = reverse_lazy('orgaos_lista')
    context_object_name = 'orgao'