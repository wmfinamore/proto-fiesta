from django.urls import path
from .views import (ProcessosListView,
                    ProcessoCreateView,
                    ProcessoUpdateView,
                    ProcessoDeleteView,
                    ProcessoDetailView,
                    CaixaListView,
                    processo_search)
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(cache_page(60 * 1)(ProcessosListView.as_view())), name='processos_lista'),
    path('novo/', ProcessoCreateView.as_view(), name='processo_novo'),
    path('detalhe/<pk>', ProcessoDetailView.as_view(), name='processo_detalhar'),
    path('editar/<pk>', ProcessoUpdateView.as_view(), name='processo_editar'),
    path('excluir/<pk>', ProcessoDeleteView.as_view(), name='processo_excluir'),
    path('caixa/', login_required(cache_page(60 * 1)(CaixaListView.as_view())), name='caixa_lista'),
    path('pesquisar/', processo_search, name='processo_search'),
]
