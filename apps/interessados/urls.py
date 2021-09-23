from django.urls import path
from .views import interessadosapi, InteressadosListView


urlpatterns = [
    path('', InteressadosListView.as_view(), name='interessados_lista'),
    path('api/', interessadosapi, name='InteressadosApi'),
]
