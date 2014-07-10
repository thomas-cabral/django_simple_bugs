from django import forms
from .models import Requirement


class RequirementForm(forms.ModelForm):

    class Meta:
        model = Requirement
        fields = ('project', 'title', 'detail', 'working_on')
        widgets = {
            'working_on': forms.SelectMultiple(attrs={'data-placeholder': 'Who is working on this?'})
        }
