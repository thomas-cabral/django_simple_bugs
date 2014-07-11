from django import forms
from .models import Case


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('project', 'type', 'title', 'detail', 'closed', 'assigned_to', 'requirement')
