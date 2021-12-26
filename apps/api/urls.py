from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import (ProcessoAPIView,
                    OrgaoAPIView,
                    AssuntoAPIView,
                    UserAPIView,
                    TramiteAPIView,
                    CaixaPostalAPIView,
                    InteressadoAPIView,
                    CargoAPIView,)


router = DefaultRouter()
router.register('processos', ProcessoAPIView)
router.register('assuntos', AssuntoAPIView)
router.register('orgaos', OrgaoAPIView)
router.register('usuarios', UserAPIView)
router.register('tramitacoes', TramiteAPIView)
router.register('interessados', InteressadoAPIView)
router.register('cargos', CargoAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('caixa/', CaixaPostalAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]
