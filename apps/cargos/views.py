from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                 )
from .models import Cargo


class CargosListView(ListView):
    model = Cargo
    context_object_name = 'cargos'


class CargoCreateView(SuccessMessageMixin, CreateView):
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
    success_url = '/success/'
    success_message = "Cargo %(nome) foi criado com sucesso!"
