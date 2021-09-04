from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ProcessoAPIView,
                    OrgaoAPIView,
                    AssuntoAPIView,
                    UserAPIView,
                    TramiteAPIView,)


router = DefaultRouter()
router.register('processos', ProcessoAPIView)
router.register('assuntos', AssuntoAPIView)
router.register('orgaos', OrgaoAPIView)
router.register('usuarios', UserAPIView)
router.register('tramitacoes', TramiteAPIView)

urlpatterns = [
    path('', include(router.urls)),
]