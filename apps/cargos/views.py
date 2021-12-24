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
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class CargosListView(ListView):
    paginate_by = 5
    model = Cargo
    context_object_name = 'cargos'


class CargoCreateView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      SuccessMessageMixin,
                      CreateView):
    permission_required = ('cargos.add_cargo')
    permission_denied_message = "Você não tem permissão para adicionar Cargos"
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
    success_url = '/cargos/'
    success_message = "Cargo foi criado com sucesso!"


class CargoEditView(LoginRequiredMixin,
                    PermissionRequiredMixin,
                    UpdateView):
    permission_required = ('cargos.change_cargo')
    permission_denied_message = "Você não tem permissão para alterar cargos"
    model = Cargo
    fields = ['classe', 'nome', 'jornada',]
    context_object_name = 'cargo'


class CargoDeleteView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      DeleteView):
    permission_required = ('cargos.delete_cargo')
    permission_denied_message = "Você não tem permissão para excluir cargos"
    model = Cargo
    success_url = reverse_lazy('cargos_lista')
    context_object_name = 'cargo'


class VinculosListView(ListView):
    paginate_by = 5
    model = Vinculo
    context_object_name = 'vinculos'


class VinculoCreateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        CreateView):
    permission_required = ('cargos.add_vinculo')
    permission_denied_message = "Você não tem permissão para adicionar vínculos"
    model = Vinculo
    form_class = VinculoForm
    success_url = '/cargos/vinculos/'
    success_message = "Vínculo foi criado com sucesso!"


class VinculoEditView(LoginRequiredMixin,
                      PermissionRequiredMixin,
                      UpdateView):
    permission_required = ('cargos.change_vinculo')
    permission_denied_message = "Você não tem permissão para alterar vínculos"
    model = Vinculo
    form_class = VinculoForm
    context_object_name = 'vinculo'


class VinculoDeleteView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        DeleteView):
    permission_required = ('cargos.delete_vinculo')
    permission_denied_message = "Você não tem permissão para excluir vínculos"
    model = Vinculo
    success_url = reverse_lazy('vinculos_lista')
    context_object_name = 'vinculo'