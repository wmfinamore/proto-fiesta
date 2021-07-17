from django.urls import path
from . import views


urlpatterns = [
    path('', views.CargosListView.as_view(), name='cargos_lista'),
    path('novo/', views.CargoCreateView.as_view(), name='cargo_novo'),
]
