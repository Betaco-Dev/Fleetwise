from django import forms
from . models import ai_predictions

class AiPredictionsForm(forms.ModelForm):
  class Meta:
    model = ai_predictions
    fields = '__all__'
    
