from django.urls import path
from .views import TramitacaoCreateView


urlpatterns = [
    path('novo/<pk>/', TramitacaoCreateView.as_view(), name='tramitacao_novo'),
]
