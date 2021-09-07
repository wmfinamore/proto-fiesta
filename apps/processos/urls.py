from django.urls import path
from .views import (ProcessosListView,
                    ProcessoCreateView,
                    ProcessoUpdateView,
                    ProcessoDeleteView,
                    CaixaListView,
                    processo_search)

urlpatterns = [
    path('', ProcessosListView.as_view(), name='processos_lista'),
    path('novo/', ProcessoCreateView.as_view(), name='processo_novo'),
    path('editar/<pk>', ProcessoUpdateView.as_view(), name='processo_editar'),
    path('excluir/<pk>', ProcessoDeleteView.as_view(), name='processo_excluir'),
    path('caixa/', CaixaListView.as_view(), name='caixa_lista'),
    path('pesquisar/', processo_search, name='processo_search'),
]
