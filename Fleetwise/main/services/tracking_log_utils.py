from Fleetwise.main.models.tracking_log import TrackingLog
from datetime import datetime, timedelta

def get_logs_for_vehicle(vehicle, start_datetime, end_datetime):
    """
    Retrieve all logs for a vehicle in a date/time range.
    """
    return TrackingLog.objects.filter(
        vehicle=vehicle,
        date_time__range=(start_datetime, end_datetime)
    ).order_by('date_time')

def reconstruct_trip_path(vehicle, date):
    """
    Reconstruct the path of a vehicle for a specific date, as a list of (lat, lon, timestamp).
    """
    logs = TrackingLog.objects.filter(
        vehicle=vehicle,
        date_time__date=date
    ).order_by('date_time')
    return [(log.latitude, log.longitude, log.date_time) for log in logs]

def detect_geofence_entries(vehicle, geofence, date):
    """
    Detect when a vehicle enters a defined geofence area on a specific date.
    Geofence should be a dictionary with 'lat_min', 'lat_max', 'lon_min', 'lon_max'.
    """
    logs = TrackingLog.objects.filter(vehicle=vehicle, date_time__date=date)
    entries = []
    for log in logs:
        if (geofence['lat_min'] <= log.latitude <= geofence['lat_max'] and
            geofence['lon_min'] <= log.longitude <= geofence['lon_max']):
            entries.append(log)
    return entries

def calculate_total_distance(vehicle, date):
    """
    Calculate the total distance traveled by a vehicle on a specific date.
    (Assumes logs are ordered and uses Haversine formula.)
    """
    import math
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371  # Earth radius in km
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        d_phi = math.radians(lat2 - lat1)
        d_lambda = math.radians(lon2 - lon1)
        a = (math.sin(d_phi/2)**2 +
             math.cos(phi1)*math.cos(phi2)*math.sin(d_lambda/2)**2)
        return 2*R*math.asin(math.sqrt(a))
    logs = TrackingLog.objects.filter(vehicle=vehicle, date_time__date=date).order_by('date_time')
    prev = None
    distance = 0
    for log in logs:
        if prev is not None:
            distance += haversine(float(prev.latitude), float(prev.longitude),
                                  float(log.latitude), float(log.longitude))
        prev = log
    return distance
