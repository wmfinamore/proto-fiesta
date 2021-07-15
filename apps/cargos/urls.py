from django.urls import path
from . import views


urlpatterns = [
    path('cargos/', views.CargosListView.as_view(), name='cargos_list'),
]
