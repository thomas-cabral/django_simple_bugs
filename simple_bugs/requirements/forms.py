from django import forms
from .models import Requirement

from simple_bugs.groups.models import Group
from simple_bugs.projects.models import Project
from django.contrib.auth.models import User


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ('project', 'title', 'detail', 'working_on')
        widgets = {
            'working_on': forms.SelectMultiple(attrs={'data-placeholder': 'Who is working on this?'})
        }
