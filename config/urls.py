"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Protocolo API",
        default_version="v1",
        description="API para o sistema de Protocolo",
        contact=openapi.Contact(email="email@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('funcionarios-autocomplete/', include('accounts.urls')),
    path('cargos/', include('apps.cargos.urls')),
    path('orgaos/', include('apps.orgaos.urls')),
    path('assuntos/', include('apps.assuntos.urls')),
    path('processos/', include('apps.processos.urls')),
    path('tramitacoes/', include('apps.tramitacoes.urls')),
    path('api/v1/', include('apps.api.urls')),
    path('interessados/', include('apps.interessados.urls')), # Criar uma rota para a api
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('tinymce/', include('tinymce.urls')),
]

# routes for activate debug toolbar when django debug mode is true
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls))
    ] + urlpatterns
