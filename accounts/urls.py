from django.urls import path
from . import views


urlpatterns = [
    # Cargos URL's
    path('', views.FuncionarioAutoComplete.as_view(), name='funcionarios_autocomplete'),
]
