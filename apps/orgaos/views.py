from django.shortcuts import render
from django.views.generic import (
                                    TemplateView,
                                    CreateView
                                 )
from .models import Orgao


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
