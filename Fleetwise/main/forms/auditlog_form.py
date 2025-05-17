from django import forms
from . models import audit_log

class AuditLogForm(forms.ModelForm):
  class Meta:
    model = audit_log
    fields = '__all__'
    
