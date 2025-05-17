from django.http import JsonResponse
from .services.route_utils import create_and_save_route

def create_optimized_route_view(request):
    # For POST requests with JSON or form data
    if request.method == 'POST':
        start_location = request.POST.get('start_location')
        end_location = request.POST.get('end_location')
        if not start_location or not end_location:
            return JsonResponse({'error': 'Both start and end locations are required.'}, status=400)
        try:
            route = create_and_save_route(start_location, end_location)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
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
