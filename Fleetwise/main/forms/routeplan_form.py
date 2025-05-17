from django import forms
from . models import route_plan
from Fleetwise.main.models.route_plan import RoutePlan

class RoutePlanForm(forms.ModelForm):
  class Meta:
    model = route_plan
    fields = '__all__'
    
