from django.shortcuts import render
from django.views.generic import ListView
from .models import Cargo


class CargosListView(ListView):
    model = Cargo
    context_object_name = 'cargos'
