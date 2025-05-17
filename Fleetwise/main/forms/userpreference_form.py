from django import forms
from . models import user_preference

class UserPreferenceForm(forms.ModelForm):
  class Meta:
    model = user_preference
    fields = '__all__'
    
