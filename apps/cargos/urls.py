from django.urls import path
from . import views


urlpatterns = [
    path('', views.CargosListView.as_view(), name='cargos_lista'),
    path('vinculos/', views.VinculosListView.as_view(), name='vinculos_lista'),
    path('novo/', views.CargoCreateView.as_view(), name='cargo_novo'),
    path('editar/<int:pk>/', views.CargoEditView.as_view(), name='cargo_editar'),
    path('excluir/<int:pk>/', views.CargoDeleteView.as_view(), name='cargo_excluir'),
]
