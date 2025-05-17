from django import forms
from . models import tracking_log


class TrackingLogForm(forms.ModelForm):
  class Meta:
    model = tracking_log
    fields = '__all__'
    
