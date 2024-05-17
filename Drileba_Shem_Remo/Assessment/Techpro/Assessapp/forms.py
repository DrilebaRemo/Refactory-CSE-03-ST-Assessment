from django.forms import ModelForm
from django import forms  
from .models import *
from django.core.exceptions import ValidationError

class RegForm(forms.ModelForm):
    class Meta:
        model = Reguser
        fields = '__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={ 'required':'required'}),
            'last_name':forms.TextInput(attrs={ 'required':'required'}),
            'course':forms.Select(attrs={'class':'form-contro', 'required':'required'}),
            'entry_scheme':forms.Select(attrs={'class':'form-contro', 'required':'required'}),
            'intake':forms.Select(attrs={'class':'form-contro', 'required':'required'}),
            'sponsorship':forms.Select(attrs={'class':'form-contro', 'required':'required'}),
            'date_of_birth':forms.DateInput(attrs={ 'required':'required'}),
            'residence':forms.TextInput(attrs={ 'required':'required'}),
        }