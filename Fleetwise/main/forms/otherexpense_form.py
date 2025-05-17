from django import forms
from . models import other_expense

class OtherExpenseForm(forms.ModelForm):
  class Meta:
    model = other_expense
    fields = '__all__'
    
