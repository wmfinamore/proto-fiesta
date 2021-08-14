from django.urls import path
from .views import TramitacaoCreateView, TramitacaoUpdateView, TramitacaoDeleteView


urlpatterns = [
    path('novo/<pk>', TramitacaoCreateView.as_view(), name='tramitacao_novo'),
    path('receber/<pk>', TramitacaoUpdateView.as_view(), name='tramitacao_receber'),
    path('excluir/<pk>', TramitacaoDeleteView.as_view(), name='tramitacao_excluir'),
]
