from django.contrib.auth.views import LoginView
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from .services.ai_service import MaintenancePredictionService, AnomalyDetectionService

# Rate-Limited Login View
class RateLimitedLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# View for Predicting Maintenance
def predict_maintenance_view(request):
    mileage = request.GET.get('mileage', None)

    if mileage is None:
        return JsonResponse({'error': 'Mileage parameter is required.'}, status=400)

    try:
        mileage = int(mileage)
        if mileage <= 0:
            return JsonResponse({'error': 'Mileage must be a positive integer.'}, status=400)

        service = MaintenancePredictionService()
        service.train_maintenance_model()  # Consider pre-training this model
        next_maintenance = service.predict_next_maintenance(mileage=mileage)
        return JsonResponse({'next_maintenance_date': next_maintenance.strftime('%Y-%m-%d')})
    except ValueError:
        return JsonResponse({'error': 'Mileage must be a valid integer.'}, status=400)
    except Exception as e:
        # Log exception here if needed
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)


# View for Detecting Anomalies
def detect_anomalies_view(request):
    gps_data = request.GET.get('gps_data', None)

    if gps_data is None:
        return JsonResponse({'error': 'GPS data parameter is required.'}, status=400)

    try:
        # Parse GPS data into a 2D array
        gps_data = [
            [float(coord) for coord in point.split(',')]
            for point in gps_data.split(';')
        ]

        # Validate GPS coordinates
        for point in gps_data:
            if not (-90 <= point[0] <= 90 and -180 <= point[1] <= 180):
                return JsonResponse({'error': 'Invalid GPS coordinates. Latitude must be between -90 and 90, and longitude between -180 and 180.'}, status=400)

        anomaly_service = AnomalyDetectionService()
        anomaly_service.train_anomaly_model(data=gps_data)
        anomalies = anomaly_service.detect_anomalies(data=gps_data)
        return JsonResponse({'anomalies': anomalies})
    except ValueError as e:
        return JsonResponse({'error': f'Invalid GPS data format. {str(e)}'}, status=400)
    except Exception as e:
        # Log exception here if needed
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
