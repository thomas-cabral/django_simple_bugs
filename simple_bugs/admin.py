__author__ = 'Thomas'
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .simple_bugs.models import Requirement, Case


class RequirementAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Requirement, RequirementAdmin)


class CaseAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Case, CaseAdmin)