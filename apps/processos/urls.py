from django.urls import path
from .views import ProcessosListView, ProcessoCreateView

urlpatterns = [
    path('', ProcessosListView.as_view(), name='processos_lista'),
    path('novo/', ProcessoCreateView.as_view(), name='processo_novo'),
]
