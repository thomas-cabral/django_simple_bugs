__author__ = 'Thomas'
from django import forms
from .models import Bug


class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
