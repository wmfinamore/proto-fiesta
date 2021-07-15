from django.urls import path
from . import views


urlpatterns = [
    path('lista/', views.CargosListView.as_view(), name='cargos_lista'),
]
