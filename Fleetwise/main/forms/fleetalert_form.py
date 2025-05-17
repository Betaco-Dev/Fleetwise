from django import forms
from . models import fleet_alert

class FleetalertForm(forms.ModelForm):
  class Meta:
    model = fleet_alert
    fields = '__all__'
    
