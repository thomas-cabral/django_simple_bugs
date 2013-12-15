__author__ = 'Thomas'
from django import forms
from django.utils.translation import ugettext as _
from .models import Case


class CaseForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = ('title', 'detail', 'requirement')