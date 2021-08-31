from django.urls import path
from .views import ProcessoAPIView


# urls para lista de processos
urlpatterns = [
    path('', ProcessoAPIView.as_view()),
]
