from django import forms
from Fleetwise.main.models import analytics_reporting

class AnalyticsReportingForm(forms.ModelForm):
  class Meta:
    model = analytics_reporting
    fields = '__all__'
    
