from django import forms
from . models import route_optimization

class RouteOptimizationForm(forms.ModelForm):
  class Meta:
    model = route_optimization
    fields = '__all__'
    
