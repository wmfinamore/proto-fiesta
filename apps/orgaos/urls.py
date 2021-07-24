from django.urls import path
from . import views


urlpatterns = [
    # Orgaos URL's
    path('', views.OrgaoListView.as_view(), name='orgaos_lista'),

]
