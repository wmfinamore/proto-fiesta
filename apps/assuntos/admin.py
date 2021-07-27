from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Assunto


class AssuntoAdmin(MPTTModelAdmin):
    model = Assunto
    raw_id_fields = ['parent']


admin.site.register(Assunto, AssuntoAdmin)
