from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet

from .models import RoutePlan
from .serializers import RoutePlanSerializer
from Fleetwise.main.forms import RoutePlanForm
from Fleetwise.main.services.route_plan_utils import check_overlapping_plans


def create_route_plan(request):
    """
    Handle the creation of a RoutePlan via a Django form.
    Prevents overlapping plans for the same vehicle.
    """
    if request.method == "POST":
        form = RoutePlanForm(request.POST)
        if form.is_valid():
            route_plan = form.save(commit=False)
            # Check for overlapping plans using the service
            if check_overlapping_plans(
                route_plan.vehicle,
                route_plan.start_date,
                route_plan.end_date
            ):
                form.add_error(None, "There is an overlapping route plan for this vehicle.")
            else:
                route_plan.save()
                return redirect('route_plan_success')  # Replace with your success URL
    else:
        form = RoutePlanForm()
    return render(request, 'route_plan_form.html', {'form': form})


class RoutePlanViewSet(ModelViewSet):
    """
    API endpoint that allows RoutePlans to be viewed or edited.
    Uses DRF's ModelViewSet for standard CRUD operations.
    """
    queryset = RoutePlan.objects.all()
    serializer_class = RoutePlanSerializer
