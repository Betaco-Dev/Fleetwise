from django.contrib.auth import authenticate, login
from django.shortcuts import render
from Fleetwise.main.models import UserLoginAttempt
from Fleetwise.main.forms import CaptchaLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CaptchaLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                form.save_login_attempt(request, success=True)
                return redirect('dashboard')  # Redirect to a dashboard or homepage
            else:
                form.save_login_attempt(request, success=False)
                form.add_error(None, "Invalid username or password.")
    else:
        form = CaptchaLoginForm()

    return render(request, 'login.html', {'form': form})
