from django.urls import path
from . import views


urlpatterns = [
    # Assuntos URL's
    path('', views.AssuntosListView.as_view(), name='assuntos_lista'),
    path('novo/', views.AssuntoCreateView.as_view(), name='assunto_novo'),
    path('editar/<int:pk>', views.AssuntoEditView.as_view(), name='assunto_editar'),
]
