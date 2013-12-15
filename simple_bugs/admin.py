__author__ = 'Thomas'
from django.contrib import admin
from .models import Requirement, Case


class RequirementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Requirement, RequirementAdmin)


class CaseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Case, CaseAdmin)