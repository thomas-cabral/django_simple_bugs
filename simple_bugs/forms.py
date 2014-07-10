__author__ = 'Thomas'
from django import forms
from simple_bugs.cases.models import Case
from simple_bugs.requirements.models import Requirement


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('project', 'type', 'title', 'detail', 'closed', 'assigned_to', 'requirement')


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ('project', 'title', 'detail', 'working_on')
        widgets = {
            'working_on': forms.SelectMultiple(attrs={'data-placeholder': 'Who is working on this?'})
        }
