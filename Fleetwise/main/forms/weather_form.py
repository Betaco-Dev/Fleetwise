from django import forms
from .models import weather
class WeatherForm(forms.ModelForm):
    class Meta:
        model = weather
        fields = '__all__'
