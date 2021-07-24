from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Orgao

class OrgaoListView(TemplateView):
    template_name = "orgaos/orgaos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orgaos'] = Orgao.objects.all()
        return context
