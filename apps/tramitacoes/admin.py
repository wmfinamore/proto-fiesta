from django.contrib import admin
from .models import Tramite
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Tramite, SimpleHistoryAdmin)
