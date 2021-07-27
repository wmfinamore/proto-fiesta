from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Assunto


admin.site.register(Assunto, MPTTModelAdmin)
