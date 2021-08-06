from django.urls import path
from .views import ProcessosListView

urlpatterns = [
    path('', ProcessosListView.as_view(), name='processos_lista'),
]
