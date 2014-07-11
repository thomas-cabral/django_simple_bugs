from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Requirement

# Register your models here.

class RequirementAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Requirement, RequirementAdmin)