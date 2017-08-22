# -*- coding: utf-8 -*-

from django import forms
from .models import Discipline

class DisciplineForm(forms.ModelForm):
    '''
        Form that refers to Discipline model.
    '''
    class Meta:
        model = Discipline
        fields = ('name', 'short', 'hours', 'email', 'active')
        labels = {'email': "Professor's E-mail"}
