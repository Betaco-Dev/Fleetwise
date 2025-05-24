from ..models.fleet_alert import FleetAlert

def create_fleet_alert(data):
    alert = FleetAlert(**data)
    alert.full_clean()
    alert.save()
    return alert

def update_fleet_alert(alert_id, data):
    alert = FleetAlert.objects.get(pk=alert_id)
    for key, value in data.items():
        setattr(alert, key, value)
    alert.full_clean()
    alert.save()
    return alert

def delete_fleet_alert(alert_id):
    alert = FleetAlert.objects.get(pk=alert_id)
    alert.delete()
