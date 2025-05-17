from django import forms
from . models import delivery_update

class DeliveryUpdateForm(forms.ModelForm):
  class Meta:
    model = delivery_update
    fields = '__all__'
    
