from django.contrib.auth.views import LoginView
from django.core.cache import cache  # Added missing import for caching
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from ratelimit.decorators import ratelimit
from django.shortcuts import render, redirect
import logging

from Fleetwise.main.forms import CaptchaLoginForm, TrackingLogForm, RoutePlanForm, OtherExpenseForm  # Fixed import for CaptchaLoginForm
from Fleetwise.main.services.tracking_log_utils import reconstruct_trip_path
from Fleetwise.main.services.route_plan_utils import check_overlapping_plans
from Fleetwise.main.services.other_expense_utils import create_other_expense
from Fleetwise.utils import notify_admin_about_failed_login  # Ensuring proper import
from Fleetwise.services.ai_service import MaintenancePredictionService, AnomalyDetectionService
from Fleetwise.utils import validate_positive_integer, parse_gps_data, validate_coordinates
from django.contrib.auth.models import User  # Ensuring correct user lookup
from datetime import date

# Constants for lockout system
LOCKOUT_THRESHOLD = 5
LOCKOUT_TIME = 900  # 15 minutes

logger = logging.getLogger(__name__)

class RateLimitedLoginView(LoginView):
    form_class = CaptchaLoginForm  # Use CAPTCHA-enabled form

    @ratelimit(key='ip', rate='5/m', block=True)
    def dispatch(self, *args, **kwargs):
        ip_address = self.request.META.get('REMOTE_ADDR')
        username = self.request.POST.get('username', 'Unknown')
        user = User.objects.filter(username=username).first()  # Fixed user lookup

        # Check if IP is locked out
        if cache.get(f"locked_out:{ip_address}"):
            return JsonResponse({'error': 'Too many failed login attempts. Try again later.', 'code': 'ACCOUNT_LOCKED'}, status=403)

        failed_attempts = cache.get(f"failed_login:{ip_address}", 0) + 1
        cache.set(f"failed_login:{ip_address}", failed_attempts, timeout=600)

        # Notify admin about failed login attempts
        notify_admin_about_failed_login(ip_address, username, failed_attempts)

        # Lock out after exceeding threshold
        if failed_attempts >= LOCKOUT_THRESHOLD:
            cache.set(f"locked_out:{ip_address}", True, timeout=LOCKOUT_TIME)
            return JsonResponse({'error': 'Too many failed login attempts. You are temporarily locked out.', 'code': 'ACCOUNT_LOCKED'}, status=403)

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
        return JsonResponse({'error': 'An unexpected error occurred. Please try again later.', 'code': 'INTERNAL_ERROR'}, status=500})


@require_POST
@login_required
def create_tracking_log(request):
    form = TrackingLogForm(request.POST)
    if form.is_valid():
        try:
            form.save()
            return redirect('tracking_log_success')
        except Exception as e:
            logger.error(f"Error saving tracking log: {str(e)}")
            form.add_error(None, "Failed to save tracking log.")
    return render(request, 'tracking_log_form.html', {'form': form})


@login_required
def create_tracking_log_form(request):
    form = TrackingLogForm()
    return render(request, 'tracking_log_form.html', {'form': form})


@login_required
def show_trip_path(request, vehicle_id, trip_date):
    try:
        trip_points = reconstruct_trip_path(vehicle_id, trip_date)
        return render(request, 'trip_path.html', {'trip_points': trip_points})
    except Exception as e:
        logger.error(f"Error reconstructing trip path: {str(e)}")
        return JsonResponse({'error': 'Failed to reconstruct trip path.', 'code': 'INTERNAL_ERROR'}, status=500})


@require_POST
@login_required
def create_route_plan(request):
    form = RoutePlanForm(request.POST)
    if form.is_valid():
        try:
            route_plan = form.save(commit=False)
            if check_overlapping_plans(route_plan.vehicle, route_plan.start_date, route_plan.end_date):
                form.add_error(None, "There is an overlapping route plan for this vehicle.")
            else:
                route_plan.save()
                return redirect('routeplan_success')
        except Exception as e:
            logger.error(f"Error creating route plan: {str(e)}")
            form.add_error(None, "Failed to create route plan.")
    return render(request, 'route_plan_form.html', {'form': form})


@login_required
def create_route_plan_form(request):
    form = RoutePlanForm()
    return render(request, 'route_plan_form.html', {'form': form})


def other_expense_create_view(request):
    if request.method == 'POST':
        form = OtherExpenseForm(request.POST)
        if form.is_valid():
            try:
                expense = create_other_expense(form.cleaned_data)
                return redirect('expense_list')  # Adjust as needed
            except Exception as e:
                logger.error(f"Error creating expense: {str(e)}")
                form.add_error(None, "Failed to create expense.")
    else:
        form = OtherExpenseForm()
    return render(request, 'other_expense_form.html', {'form': form})
