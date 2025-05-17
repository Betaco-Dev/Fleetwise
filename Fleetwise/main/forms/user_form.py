from django import forms
from .models import user

class UserForm(models.ModelForm):
  class Meta:
    model = fleetalert
