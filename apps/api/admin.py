from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin


# Torna o campo usuário pesquisável para geração de tokens pelo módulo admin
TokenAdmin.raw_id_fields = ['user']
