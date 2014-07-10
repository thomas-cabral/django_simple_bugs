from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Case
# Register your models here.


class CaseAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Case, CaseAdmin)