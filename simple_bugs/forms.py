__author__ = 'Thomas'
from django import forms
from django.utils.translation import ugettext as _
from .models import Case, Requirement


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('type', 'title', 'detail', 'requirement')


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ('title', 'detail')