from django.urls import path
from .custom_views import RateLimitedLoginView, predict_maintenance_view, detect_anomalies_view

# Custom Views URL Patterns
urlpatterns = [
    path('login/', RateLimitedLoginView.as_view(), name='login'),
    path('predict-maintenance/', predict_maintenance_view, name='predict_maintenance'),
    path('detect-anomalies/', detect_anomalies_view, name='detect_anomalies'),
]
