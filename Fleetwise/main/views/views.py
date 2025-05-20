from django.contrib.auth.views import LoginView
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from .services.ai_service import MaintenancePredictionService, AnomalyDetectionService
from .utils import validate_positive_integer, parse_gps_data, validate_coordinates
from django.shortcuts import render, redirect
from Fleetwise.main.forms import TrackingLogForm, RoutePlanForm, OtherExpenseForm
from Fleetwise.main.services.tracking_log_utils import reconstruct_trip_path
from Fleetwise.main.services.route_plan_utils import check_overlapping_plans
from Fleetwise.main.services.other_expense_utils import create_other_expense
from datetime import date
import logging

logger = logging.getLogger(__name__)

class RateLimitedLoginView(LoginView):
    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        logger.info(f"Rate-limited login attempt. IP: {self.request.META.get('REMOTE_ADDR')}")
        return super().dispatch(*args, **kwargs)

@require_GET
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

@require_GET
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

@require_POST
@login_required
def create_tracking_log(request):
    form = TrackingLogForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('tracking_log_success')
    return render(request, 'tracking_log_form.html', {'form': form})

@login_required
def create_tracking_log_form(request):
    form = TrackingLogForm()
    return render(request, 'tracking_log_form.html', {'form': form})

@login_required
def show_trip_path(request, vehicle_id, trip_date):
    trip_points = reconstruct_trip_path(vehicle_id, trip_date)
    return render(request, 'trip_path.html', {'trip_points': trip_points})

@require_POST
@login_required
def create_route_plan(request):
    form = RoutePlanForm(request.POST)
    if form.is_valid():
        route_plan = form.save(commit=False)
        if check_overlapping_plans(route_plan.vehicle, route_plan.start_date, route_plan.end_date):
            form.add_error(None, "There is an overlapping route plan for this vehicle.")
        else:
            route_plan.save()
            return redirect('routeplan_success')
    return render(request, 'route_plan_form.html', {'form': form})

@login_required
def create_route_plan_form(request):
    form = RoutePlanForm()
    return render(request, 'route_plan_form.html', {'form': form})

def other_expense_create_view(request):
    if request.method == 'POST':
        form = OtherExpenseForm(request.POST)
        if form.is_valid():
            expense = create_other_expense(form.cleaned_data)
            return redirect('expense_list')  # Adjust as needed
    else:
        form = OtherExpenseForm()
    return render(request, 'other_expense_form.html', {'form': form})
