from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from Fleetwise.main.models import UserLoginAttempt

class CaptchaLoginForm(AuthenticationForm):
    captcha = ReCaptchaField()

    def save_login_attempt(self, request, success=False):
        """Saves login attempt details in the database."""
        ip_address = request.META.get('REMOTE_ADDR')
        user = User.objects.filter(username=self.cleaned_data.get("username")).first()

        UserLoginAttempt.objects.create(
            user=user,
            ip_address=ip_address,
            success=success
        )
