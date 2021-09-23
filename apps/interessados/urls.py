from django.urls import path
from .views import interessadosapi, InteressadosListView, InteressadoCreateView


urlpatterns = [
    path('', InteressadosListView.as_view(), name='interessados_lista'),
    path('novo/', InteressadoCreateView.as_view(), name='interessado_novo'),
    path('api/', interessadosapi, name='InteressadosApi'),
]
