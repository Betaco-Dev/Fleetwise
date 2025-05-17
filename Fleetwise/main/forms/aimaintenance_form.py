from django import forms
from . models import ai_maintenance

class AiMaintenanceForm(forms.ModelForm):
  class Meta:
    model = ai_maintenance
    fields = '__all__'
    
