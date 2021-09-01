from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProcessoAPIView


router = SimpleRouter()
router.register('', ProcessoAPIView, basename='processos')

urlpatterns = router.urls
