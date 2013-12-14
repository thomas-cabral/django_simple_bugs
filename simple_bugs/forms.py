__author__ = 'Thomas'
from django import forms
from django.utils.translation import ugettext as _
from .models import Bug


class BugForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('title', 'detail', 'requirement')