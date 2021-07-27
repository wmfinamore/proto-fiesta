from django.contrib.admin.apps import AdminConfig


class ProtoAdminConfig(AdminConfig):
    default_site = 'config.admin.ProtoAdminSite'
