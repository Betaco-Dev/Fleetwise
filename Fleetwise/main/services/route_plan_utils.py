from Fleetwise.main.models.route_plan import RoutePlan

def check_overlapping_plans(vehicle, start_date, end_date):
    """
    Check if there are any other plans for this vehicle that overlap with the given dates.
    """
    return RoutePlan.objects.filter(
        vehicle=vehicle,
        start_date__lte=end_date,
        end_date__gte=start_date
    ).exists()

def generate_route_plan_summary(route_plan):
    """
    Return a dictionary summary of the route plan.
    """
    return {
        "id": route_plan.id,
        "vehicle": str(route_plan.vehicle),
        "user": str(route_plan.user),
        "date_range": f"{route_plan.start_date} to {route_plan.end_date}",
        "description": route_plan.description
    }

def plans_for_user(user, start_date=None, end_date=None):
    """
    Retrieve all plans for a user, optionally filtered by date range.
    """
    qs = RoutePlan.objects.filter(user=user)
    if start_date and end_date:
        qs = qs.filter(
            start_date__lte=end_date,
            end_date__gte=start_date
        )
    return qs.order_by('start_date')
