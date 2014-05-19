__author__ = 'Thomas'
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Requirement, Case, Estimate, Project


class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)


class RequirementAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Requirement, RequirementAdmin)


class CaseAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Case, CaseAdmin)


class EstimateAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Estimate, EstimateAdmin)