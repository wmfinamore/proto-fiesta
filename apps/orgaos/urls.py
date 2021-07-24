from django.urls import path
from . import views


urlpatterns = [
    # Orgaos URL's
    path('', views.OrgaosListView.as_view(), name='orgaos_lista'),
    path('novo/', views.OrgaoCreateView.as_view(), name='orgao_novo'),
    path('editar/<int:pk>/', views.OrgaoEditView.as_view(), name='orgao_editar'),

]
