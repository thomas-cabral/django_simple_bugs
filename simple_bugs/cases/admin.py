from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Case, TestStep, TestCase
# Register your models here.


class CaseAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(Case, CaseAdmin)


class TestStepAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(TestStep, TestStepAdmin)


class TestCaseAdmin(SimpleHistoryAdmin):
    pass
admin.site.register(TestCase, TestCaseAdmin)