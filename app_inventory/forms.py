# forms.py
from django import forms
from .models import departmentsdb

class DepartForm(forms.ModelForm):
    
    class Meta:
        model = departmentsdb
        fields = ['depar_cod', 'depar_name']
