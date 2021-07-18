from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                 )
from .models import Cargo
from .models import Vinculo
from .forms import VinculoForm


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
    context_object_name = 'cargo'


class CargoDeleteView(DeleteView):
    model = Cargo
    success_url = reverse_lazy('cargos_lista')
    context_object_name = 'cargo'


class VinculosListView(ListView):
    model = Vinculo
    context_object_name = 'vinculos'