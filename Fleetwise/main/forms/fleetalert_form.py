from django import forms
from . models import fleetalert

class FleetalertForm(forms.ModelForm):
  class Meta:
    model = fleetalert
    fields = '__all__'
    
