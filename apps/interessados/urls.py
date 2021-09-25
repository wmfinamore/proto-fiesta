from django.urls import path
from .views import interessadosapi, InteressadosListView, InteressadoCreateView, InteressadoUpdateView


urlpatterns = [
    path('', InteressadosListView.as_view(), name='interessados_lista'),
    path('novo/', InteressadoCreateView.as_view(), name='interessado_novo'),
    path('editar/<int:pk>/', InteressadoUpdateView.as_view(), name='interessado_editar'),
    path('api/', interessadosapi, name='InteressadosApi'),
]
