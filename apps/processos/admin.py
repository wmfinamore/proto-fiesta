from django.contrib import admin
from .models import Processo
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Processo, SimpleHistoryAdmin)
