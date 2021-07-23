from django.urls import path
from . import views


urlpatterns = [
    # Orgaos URL's
    path('', views.OrgaosList, name='orgaos_lista'),

]
