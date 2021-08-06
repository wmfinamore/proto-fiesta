from django.views.generic import ListView
from .models import Processo

class ProcessosListView(ListView):
    model = Processo
    context_object_name = 'processos'
