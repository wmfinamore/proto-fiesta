from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                 )
from .models import Cargo


class CargosListView(ListView):
    model = Cargo
    context_object_name = 'cargos'


class CargoCreateView(SuccessMessageMixin, CreateView):
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
    success_url = '/cargos/'
    success_message = "Cargo foi criado com sucesso!"


class CargoEditView(UpdateView):
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
