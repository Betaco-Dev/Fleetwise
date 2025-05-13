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
    extra = 0  # Do not show empty rows by default

class MaintenanceScheduleInline(admin.TabularInline):
    model = MaintenanceSchedule
    extra = 0

# DeliveryUpdate Model
@admin.register(DeliveryUpdate)
class DeliveryUpdateAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'status', 'update_timestamp')
    search_fields = ('user__username', 'vehicle__license_plate', 'status')
    list_filter = ('update_timestamp', 'status')  # Added 'status' filter for better usability

# Vehicle Model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('type', 'license_plate', 'model', 'year')
    search_fields = ('license_plate', 'model')
    list_filter = ('type', 'year')
    list_editable = ('model', 'year')  # Allow quick editing in the list view

# TrackingLog Model
@admin.register(TrackingLog)
class TrackingLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'date_time', 'latitude', 'longitude')
    search_fields = ('user__username', 'vehicle__license_plate')
    list_filter = ('date_time',)
    readonly_fields = ('latitude', 'longitude')
    ordering = ('-date_time',)  # Default ordering by most recent logs

# MaintenanceSchedule Model
@admin.register(MaintenanceSchedule)
class MaintenanceScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'maintenance_date', 'description', 'amount', 'currency')
    search_fields = ('user__username', 'vehicle__license_plate', 'description')
    list_filter = ('maintenance_date', 'currency')

# FuelExpense Model
@admin.register(FuelExpense)
class FuelExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'date', 'amount', 'currency')
    search_fields = ('user__username', 'vehicle__license_plate')
    list_filter = (('date', admin.DateFieldListFilter), 'currency')

# RouteOptimization Model
@admin.register(RouteOptimization)
class RouteOptimizationAdmin(admin.ModelAdmin):
    list_display = ('start_location', 'end_location', 'optimized_route')
    search_fields = ('start_location', 'end_location')

    @admin.action(description='Clear Optimized Routes')
    def clear_routes(self, request, queryset):
        queryset.update(optimized_route="Cleared")
        self.message_user(request, "Optimized routes have been cleared.")

    actions = [clear_routes]

# RoutePlan Model
@admin.register(RoutePlan)
class RoutePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'start_date', 'end_date')
    search_fields = ('user__username', 'vehicle__license_plate')
    list_filter = ('start_date', 'end_date')

# OtherExpense Model
@admin.register(OtherExpense)
class OtherExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'currency', 'date')
    search_fields = ('description',)
    list_filter = ('date', 'currency')

# DeliveryUpdate Model
@admin.register(DeliveryUpdate)
class DeliveryUpdateAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'status', 'update_timestamp')
    search_fields = ('user__username', 'vehicle__license_plate', 'status')
    list_filter = ('update_timestamp',)

# AnalyticsReport Model
@admin.register(AnalyticsReport)
class AnalyticsReportAdmin(admin.ModelAdmin):
    list_display = ('report_name', 'created_date')
    search_fields = ('report_name',)
    list_filter = ('created_date',)

# Currency Model
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('currency_code', 'currency_name')
    search_fields = ('currency_code', 'currency_name')

# UserPreferences Model
@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'notifications_enabled')
    list_filter = ('theme', 'notifications_enabled')
    search_fields = ('user__username',)

# AiMaintenance Model
@admin.register(AiMaintenance)
class AiMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'maintenance_date')
    search_fields = ('vehicle__license_plate',)

# AiPredictions Model
@admin.register(AiPredictions)
class AiPredictionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'prediction_type', 'prediction_date', 'prediction_result')
    search_fields = ('user__username', 'vehicle__license_plate', 'prediction_result')
    list_filter = ('prediction_result', 'prediction_type', 'prediction_date')

# WeatherCondition Model
@admin.register(WeatherCondition)
class WeatherConditionAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'temperature', 'condition')
    list_filter = ('condition', 'date')
    search_fields = ('location',)

# FleetAlert Model
@admin.register(FleetAlert)
class FleetAlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'alert_type', 'alert_message', 'created_at')
    search_fields = ('alert_type', 'vehicle__license_plate', 'alert_message')
    list_filter = ('created_at', 'alert_type')

    @admin.action(description='Mark selected alerts as resolved')
    def mark_as_resolved(self, request, queryset):
        queryset.update(alert_message="Resolved")
        self.message_user(request, "Selected alerts have been marked as resolved.")

    actions = [mark_as_resolved]

