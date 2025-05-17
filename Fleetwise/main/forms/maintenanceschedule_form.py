from django import forms
from . models import maintenance_schedule

class MaintenanceScheduleForm(forms.ModelForm):
  class Meta:
    model = maintenance_schedule
    fields = '__all__'
    
