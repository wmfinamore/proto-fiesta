from django.urls import path
from .views import (TramitacaoCreateView,
                    TramitacaoUpdateView,
                    TramitacaoDeleteView,
                    ExportarTramitesCSV,
                    TramitesNaoRecebidos,)


urlpatterns = [
    path('novo/<pk>', TramitacaoCreateView.as_view(), name='tramitacao_novo'),
    path('receber/<pk>', TramitacaoUpdateView.as_view(), name='tramitacao_receber'),
    path('excluir/<pk>', TramitacaoDeleteView.as_view(), name='tramitacao_excluir'),
    path('exportar-tramites-csv/<pk>', ExportarTramitesCSV.as_view(), name='exportar_tramites_csv'),
    path('tramites-nao-recebidos/', TramitesNaoRecebidos.as_view(), name='tramites_nao_recebidos'),
]
