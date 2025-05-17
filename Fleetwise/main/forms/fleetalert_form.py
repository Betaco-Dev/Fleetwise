from django import forms
from . models import fleet_alert

class FleetalertForm(forms.ModelForm):
  class Meta:
    model = fleetalert
    fields = '__all__'
    
