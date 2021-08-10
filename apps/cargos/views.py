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
from django.contrib.auth.mixins import LoginRequiredMixin


class CargosListView(ListView):
    model = Cargo
    context_object_name = 'cargos'


class CargoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
    success_url = '/cargos/'
    success_message = "Cargo foi criado com sucesso!"


class CargoEditView(LoginRequiredMixin, UpdateView):
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
    context_object_name = 'cargo'


class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    success_url = reverse_lazy('cargos_lista')
    context_object_name = 'cargo'


class VinculosListView(ListView):
    model = Vinculo
    context_object_name = 'vinculos'


class VinculoCreateView(LoginRequiredMixin, CreateView):
    model = Vinculo
    form_class = VinculoForm
    success_url = '/cargos/vinculos/'
    success_message = "Vínculo foi criado com sucesso!"


class VinculoEditView(LoginRequiredMixin, UpdateView):
    model = Vinculo
    form_class = VinculoForm
    context_object_name = 'vinculo'


class VinculoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vinculo
    success_url = reverse_lazy('vinculos_lista')
    context_object_name = 'vinculo'