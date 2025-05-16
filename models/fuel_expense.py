from django.db import models
from .user import User
from .vehicle import Vehicle

class FuelExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"Fuel Expense {self.id} - {self.user.name}"

    @classmethod
    def total_expenses_for_user(cls, user, start_date, end_date):
        """
        Calculate total fuel expenses for a given user within a date range.
        """
        return cls.objects.filter(
            user=user, date__range=(start_date, end_date)
        ).aggregate(total=models.Sum('amount'))['total'] or 0

    @classmethod
    def total_expenses_for_vehicle(cls, vehicle, start_date, end_date):
        """
        Calculate total fuel expenses for a given vehicle within a date range.
        """
        return cls.objects.filter(
            vehicle=vehicle, date__range=(start_date, end_date)
        ).aggregate(total=models.Sum('amount'))['total'] or 0
