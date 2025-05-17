from Fleetwise.main.models.fuel_expense import FuelExpense

def total_expenses_for_user(user, start_date, end_date):
    return FuelExpense.objects.filter(
        user=user, date__range=(start_date, end_date)
    ).aggregate(total=models.Sum('amount'))['total'] or 0

def total_expenses_for_vehicle(vehicle, start_date, end_date):
    return FuelExpense.objects.filter(
        vehicle=vehicle, date__range=(start_date, end_date)
    ).aggregate(total=models.Sum('amount'))['total'] or 0
