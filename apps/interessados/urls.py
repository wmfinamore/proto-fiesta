from django.urls import path
from .views import (interessadosapi,
                    InteressadosListView,
                    InteressadoCreateView,
                    InteressadoUpdateView,
                    InteressadoDeleteView,)


urlpatterns = [
    path('', InteressadosListView.as_view(), name='interessados_lista'),
    path('novo/', InteressadoCreateView.as_view(), name='interessado_novo'),
    path('editar/<pk>/', InteressadoUpdateView.as_view(), name='interessado_editar'),
    path('excluir/<pk>/', InteressadoDeleteView.as_view(), name='interessado_excluir'),
    path('api/', interessadosapi, name='InteressadosApi'),
]
