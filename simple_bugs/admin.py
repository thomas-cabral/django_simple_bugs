__author__ = 'Thomas'
from django.contrib import admin
from .models import Requirement, Bug

class RequirementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Requirement, RequirementAdmin)

class BugAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bug, BugAdmin)