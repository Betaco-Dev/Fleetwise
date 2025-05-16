from django.contrib import admin
from .models import (
    Admin, User, Vehicle, TrackingLog, MaintenanceSchedule, FuelExpense,
    RouteOptimization, RoutePlan, OtherExpense, DeliveryUpdate, AnalyticsReport, Currency, UserPreferences, AiMaintenance, AiPredictions, AuditLog,
    FleetAlert, Signals, Tests, WeatherCondition
)

# Admin Model
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

# Inline for related models
class TrackingLogInline(admin.TabularInline):
    model = TrackingLog
    extra = 0

class MaintenanceScheduleInline(admin.TabularInline):
    model = MaintenanceSchedule
    extra = 0

# User Model with inlines and actions
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'license_number', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    inlines = [TrackingLogInline, MaintenanceScheduleInline]

    @admin.action(description='Reset selected users to Riders')
    def reset_to_riders(self, request, queryset):
        queryset.update(role='Rider')
        self.message_user(request, "Selected users' roles have been reset to Riders.")

    actions = [reset_to_riders]

# ... (rest of your model registrations remain as you had)
