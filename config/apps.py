from django.contrib.admin.apps import AdminConfig


class AssuntoAdminConfig(AdminConfig):
    default_site = 'config.admin.ProtoAdminSite'
