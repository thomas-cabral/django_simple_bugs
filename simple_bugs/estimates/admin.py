from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Estimate
# Register your models here.


class EstimateAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Estimate, EstimateAdmin)