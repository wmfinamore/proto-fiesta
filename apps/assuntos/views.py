from django.views.generic import ListView
from .models import Assunto


class AssuntosListView(ListView):
    model = Assunto
    context_object_name = 'assuntos'
