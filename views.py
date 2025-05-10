from django.contrib.auth.views import LoginView
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from .services.ai_service import MaintenancePredictionService, AnomalyDetectionService
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Rate-Limited Login View
class RateLimitedLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        logger.info("Rate-limited login attempt.")
        return super().dispatch(*args, **kwargs)

# View for Predicting Maintenance
def predict_maintenance_view(request):
    mileage = request.GET.get('mileage', None)
    if mileage is None:
        logger.warning("Maintenance prediction request missing 'mileage' parameter.")
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
        logger.error("Invalid mileage value provided for maintenance prediction.")
        return JsonResponse({'error': 'Mileage must be a valid integer.'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error during maintenance prediction: {str(e)}")
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

# View for Detecting Anomalies
def detect_anomalies_view(request):
    gps_data = request.GET.get('gps_data', None)
    if gps_data is None:
        logger.warning("Anomaly detection request missing 'gps_data' parameter.")
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
        logger.error(f"Invalid GPS data format provided: {str(e)}")
        return JsonResponse({'error': f'Invalid GPS data format. {str(e)}'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error during anomaly detection: {str(e)}")
        return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
