from django.test import TestCase
from .models import MaintenanceSchedule, User, Vehicle
from django.core.exceptions import ValidationError

class MaintenanceScheduleTest(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.user = User.objects.create(name="Test User")
        self.vehicle = Vehicle.objects.create(name="Test Vehicle")

    def test_negative_amount(self):
        schedule = MaintenanceSchedule(
            user=self.user,
            vehicle=self.vehicle,
            amount=-100.00,
            maintenance_date="2025-01-01",
            description="Test Maintenance",
            currency="USD",
        )
        with self.assertRaises(ValidationError):
            schedule.clean()

    def test_valid_maintenance_schedule(self):
        schedule = MaintenanceSchedule(
            user=self.user,
            vehicle=self.vehicle,
            amount=150.00,
            maintenance_date="2025-01-01",
            description="Test Maintenance",
            currency="USD",
        )
        try:
            schedule.clean()  # This should not raise any exception
        except ValidationError:
            self.fail("ValidationError raised unexpectedly!")
