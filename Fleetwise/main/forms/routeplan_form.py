from django import forms
from Fleetwise.main.models.route_plan import RoutePlan

class RoutePlanForm(forms.ModelForm):
    class Meta:
        model = RoutePlan
        fields = '__all__'
