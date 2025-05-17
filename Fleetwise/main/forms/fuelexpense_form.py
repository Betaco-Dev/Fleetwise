from django import forms
from . models import fuel_expense

class FuelExpenseForm(forms.ModelForm):
  class Meta:
    model = fuel_expense
    fields = '__all__'
    
