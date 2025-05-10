from django.urls import path
from .views import RateLimitedLoginView

urlpatterns = [
    path('login/', RateLimitedLoginView.as_view(), name='login'),
    # Other URLs...
]
