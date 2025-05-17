#Maintenance and anomaly detection
from django.contrib.auth.views import LoginView
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services.ai_service import MaintenancePredictionService, AnomalyDetectionService
from .utils import validate_positive_integer, parse_gps_data, validate_coordinates
#Tracking log
from django.shortcuts import render, redirect
from Fleetwise.main.forms import TrackingLogForm
from Fleetwise.main.services.tracking_log_utils import reconstruct_trip_path
from datetime import date

#Routeplan
from django.shortcuts import render, redirect
from Fleetwise.main.forms import RoutePlanForm
from Fleetwise.main.services.route_plan_utils import check_overlapping_plans


import logging

logger = logging.getLogger(__name__)

class RateLimitedLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        logger.info(f"Rate-limited login attempt. IP: {self.request.META.get('REMOTE_ADDR')}")
        return super().dispatch(*args, **kwargs)

#Maintainance prediction
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

#Anomaly detection
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
        
#Tracking log

    def create_tracking_log(request):
    if request.method == "POST":
        form = TrackingLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracking_log_success')  # Replace with your URL
    else:
        form = TrackingLogForm()
    return render(request, 'tracking_log_form.html', {'form': form})

def show_trip_path(request, vehicle_id, trip_date):
    # trip_date as "YYYY-MM-DD"
    trip_points = reconstruct_trip_path(vehicle_id, trip_date)
    return render(request, 'trip_path.html', {'trip_points': trip_points})

    #Routeplan
    def create_route_plan(request):
    if request.method == "POST":
        form = RoutePlanForm(request.POST)
        if form.is_valid():
            route_plan = form.save(commit=False)
            if check_overlapping_plans(route_plan.vehicle, route_plan.start_date, route_plan.end_date):
                form.add_error(None, "There is an overlapping route plan for this vehicle.")
            else:
                route_plan.save()
                return redirect('routeplan_success')  # Replace with your own success URL or view
    else:
        form = RoutePlanForm()
    return render(request, 'route_plan_form.html', {'form': form})
        
        #Jsonresponse upon error
    except ValueError as e:
        logger.error(f"Validation error for GPS data: {str(e)}")
        return JsonResponse({'error': f'Invalid GPS data format. {str(e)}', 'code': 'VALIDATION_ERROR'}, status=400)
    except Exception as e:
        logger.error(f"Unexpected error during anomaly detection: {str(e)}")
        return JsonResponse({'error': 'An unexpected error occurred. Please try again later.', 'code': 'INTERNAL_ERROR'}, status=500)
