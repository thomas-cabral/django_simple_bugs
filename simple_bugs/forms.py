__author__ = 'Thomas'
from django import forms
from django.utils.translation import ugettext as _
from .models import Case, Requirement


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('type', 'title', 'detail', 'assigned_to', 'requirement')


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ('title', 'detail', 'working_on')
        widgets = {
            'working_on': forms.SelectMultiple(attrs={'data-placeholder': 'Who is working on this?'})
        }