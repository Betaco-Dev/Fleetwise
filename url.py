from django.urls import path
from .views import RateLimitedLoginView
from . import views

urlpatterns = [
    path('login/', RateLimitedLoginView.as_view(), name='login'),
    path('predict-maintenance/', views.predict_maintenance_view, name='predict_maintenance'),
    path('detect-anomalies/', views.detect_anomalies_view, name='detect_anomalies'),
]
