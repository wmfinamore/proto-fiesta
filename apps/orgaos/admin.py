from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Orgao


class OrgaoAdmin(MPTTModelAdmin):
    model = Orgao


admin.site.register(Orgao, OrgaoAdmin)
