from django.http import JsonResponse
from .services.route_utils import compute_route_and_stats
from .models import RouteOptimization

def create_optimized_route_view(request):
    # For POST requests with JSON or form data
    if request.method == 'POST':
        start_location = request.POST.get('start_location')
        end_location = request.POST.get('end_location')
        if not start_location or not end_location:
            return JsonResponse({'error': 'Both start and end locations are required.'}, status=400)
        stats = compute_route_and_stats(start_location, end_location)
        route = RouteOptimization.objects.create(
            start_location=start_location,
            end_location=end_location,
            optimized_route=str(stats['route_coords']),
            distance=stats['distance_km'],
            duration=stats['duration_min'],
        )
        return JsonResponse({
            'id': route.id,
            'start_location': route.start_location,
            'end_location': route.end_location,
            'distance': route.distance,
            'duration': route.duration,
            'optimized_route': route.optimized_route,
        })
    else:
        return JsonResponse({'error': 'POST request required.'}, status=405)
