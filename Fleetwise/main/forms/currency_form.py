from django import forms
from . models import currency

class CurrencyForm(forms.ModelForm):
  class Meta:
    model = currency
    fields = '__all__'
    
