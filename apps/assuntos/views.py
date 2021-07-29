from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                 )
from .models import Assunto


class AssuntosListView(ListView):
    model = Assunto
    context_object_name = 'assuntos'


class AssuntoCreateView(CreateView):
    model = Assunto
    fields = ['nome', 'parent', 'situacao']
    success_url = '/assuntos/'
    success_message = 'Assuntos criado com sucesso!'


class AssuntoEditView(UpdateView):
    model = Assunto
    fields = ['nome', 'parent', 'situacao']
    context_object_name = 'assunto'

