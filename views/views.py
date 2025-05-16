from django.contrib.auth.views import LoginView
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services.ai_service import MaintenancePredictionService, AnomalyDetectionService
from .utils import validate_positive_integer, parse_gps_data, validate_coordinates
import logging

logger = logging.getLogger(__name__)

class RateLimitedLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        logger.info(f"Rate-limited login attempt. IP: {self.request.META.get('REMOTE_ADDR')}")
        return super().dispatch(*args, **kwargs)

@ratelimit(key='ip', rate='10/m', block=True)
@login_required
def predict_maintenance_view(request):
    mileage = request.GET.get('mileage')
    if mileage is None:
        logger.warning(f"Missing 'mileage' parameter. IP: {request.META.get('REMOTE_ADDR')}")
        return JsonResponse({'error': 'Mileage parameter is required.', 'code': 'MISSING_PARAMETER'}, status=400)

    try:
        mileage = validate_positive_integer(mileage, "Mileage must be a positive integer.")
        service = MaintenancePredictionService()
        next_maintenance = service.predict_next_maintenance(mileage=mileage)
        return JsonResponse({'next_maintenance_date': next_maintenance.strftime('%Y-%m-%d')})
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return JsonResponse({'error': str(e), 'code': 'VALIDATION_ERROR'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error during maintenance prediction: {str(e)}")
        return JsonResponse({'error': 'An unexpected error occurred. Please try again later.', 'code': 'INTERNAL_ERROR'}, status=500)

@ratelimit(key='ip', rate='10/m', block=True)
@login_required
def detect_anomalies_view(request):
    gps_data = request.GET.get('gps_data')
    if gps_data is None:
        logger.warning(f"Missing 'gps_data' parameter. IP: {request.META.get('REMOTE_ADDR')}")
        return JsonResponse({'error': 'GPS data parameter is required.', 'code': 'MISSING_PARAMETER'}, status=400)

    try:
        gps_data = parse_gps_data(gps_data)
        validate_coordinates(gps_data)

        anomaly_service = AnomalyDetectionService()
        anomalies = anomaly_service.detect_anomalies(data=gps_data)
        return JsonResponse({'anomalies': anomalies})
    except ValueError as e:
        logger.error(f"Validation error for GPS data: {str(e)}")
        return JsonResponse({'error': f'Invalid GPS data format. {str(e)}', 'code': 'VALIDATION_ERROR'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error during anomaly detection: {str(e)}")
        return JsonResponse({'error': 'An unexpected error occurred. Please try again later.', 'code': 'INTERNAL_ERROR'}, status=500)
