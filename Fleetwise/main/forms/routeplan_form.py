from django import forms
from . models import froute_plan

class RoutePlanForm(forms.ModelForm):
  class Meta:
    model = route_plan
    fields = '__all__'
    
