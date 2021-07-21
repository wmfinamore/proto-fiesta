from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Orgao

admin.site.register(Orgao, MPTTModelAdmin)