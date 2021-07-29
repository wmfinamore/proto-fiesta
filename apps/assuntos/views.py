from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                 )
from .models import Assunto
from django.urls import reverse_lazy


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


class AssuntoDeleView(DeleteView):
    model = Assunto
    context_object_name = 'assunto'
    success_url = reverse_lazy('assuntos_lista')
