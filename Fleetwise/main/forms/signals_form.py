from django import forms
from . models import signals

class SignalsalertForm(forms.ModelForm):
  class Meta:
    model = signals
    fields = '__all__'
    
