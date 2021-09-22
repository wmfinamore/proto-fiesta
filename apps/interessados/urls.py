from django.urls import path
from .views import interessadosapi


# criar uma url para a view que retorna os dados
urlpatterns = [
    path('api/', interessadosapi, name='InteressadosApi'),
]
