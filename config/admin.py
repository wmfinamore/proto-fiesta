from django.contrib.admin import AdminSite


class ProtoAdminSite(AdminSite):
    site_header = 'Administração do Protocolo'
    site_title = 'Administração do Protocolo'
    index_title = 'Administração do Sistema'
