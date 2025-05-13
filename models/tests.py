from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import MaintenanceSchedule, User, Vehicle, UserPreference, ThemeChoices


class MaintenanceScheduleTest(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.user = User.objects.create(name="Test User")
        self.vehicle = Vehicle.objects.create(name="Test Vehicle")

    def test_negative_amount(self):
        """
        Test that a MaintenanceSchedule with a negative amount raises a ValidationError.
        """
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
        """
        Test that a valid MaintenanceSchedule passes validation.
        """
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


class UserPreferenceTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(username='test_user')

    def test_default_theme(self):
        """
        Test that the default theme for a UserPreference is LIGHT.
        """
        preference = UserPreference.objects.create(user=self.user)
        self.assertEqual(preference.theme, ThemeChoices.LIGHT)

    def test_update_theme(self):
        """
        Test that the theme in UserPreference can be updated successfully.
        """
        preference = UserPreference.objects.create(user=self.user)
        preference.theme = ThemeChoices.DARK
        preference.save()
        self.assertEqual(preference.theme, ThemeChoices.DARK)
