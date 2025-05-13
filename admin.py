from django.contrib import admin
from .models import (
    Admin, User, Vehicle, TrackingLog, MaintenanceSchedule, FuelExpense,
    RouteOptimization, RoutePlan, OtherExpense, DeliveryUpdate, AnalyticsReport, Currency, UserPreferences, AiMaintenance, AiPredictions, AuditLog,
    FleetAlert, RoutePlan, Signals, Tests, Weather
)

# Register each model to make it manageable in the admin panel
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(TrackingLog)
admin.site.register(MaintenanceSchedule)
admin.site.register(FuelExpense)
admin.site.register(RouteOptimization)
admin.site.register(RoutePlan)
admin.site.register(OtherExpense)
admin.site.register(DeliveryUpdate)
admin.site.register(AnalyticsReport)
admin.site.register(Currency)
admin.site.register(User_Preferences)
admin.site.register(AiMaintenance)
admin.site.register(AiPredictions)
admin.site.register(AuditLog)
admin.site.register(FleetAlert)
admin.site.register(RoutePlan)
admin.site.register(Signals)
admin.site.register(Tests)
admin.site.register(Weather)

from django.contrib import admin
from .models import (
    Admin, User, Vehicle, TrackingLog, MaintenanceSchedule, FuelExpense,
    RouteOptimization, RoutePlan, OtherExpense, DeliveryUpdate, AnalyticsReport, Currency, User_Preferences, AiMaintenance, AiPredictions, AuditLog,
    FleetAlert, RoutePlan, Signals, Tests, Weather

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

# User Model with inlines and actions
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'license_number', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone')
    inlines = [TrackingLogInline, MaintenanceScheduleInline]  # Add related inlines

    # Custom action to reset user roles
    @admin.action(description='Reset selected users to Riders')
    def reset_to_riders(self, request, queryset):
        queryset.update(role='Rider')
        self.message_user(request, "Selected users' roles have been reset to Riders.")

    actions = [reset_to_riders]

# Vehicle Model with editable fields
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('type', 'license_plate', 'model', 'year', 'editable_field')
    search_fields = ('license_plate', 'model')
    list_filter = ('type', 'year')
    list_editable = ('model', 'year')  # Allow quick editing in the list view

# TrackingLog Model with read-only fields
@admin.register(TrackingLog)
class TrackingLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'date_time', 'latitude', 'longitude')
    search_fields = ('user__name', 'vehicle__license_plate')
    list_filter = ('date_time',)
    readonly_fields = ('latitude', 'longitude')  # Fields cannot be edited

# MaintenanceSchedule Model with custom forms
@admin.register(MaintenanceSchedule)
class MaintenanceScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'maintenance_date', 'description', 'amount', 'currency')
    search_fields = ('user__name', 'vehicle__license_plate', 'description')
    list_filter = ('maintenance_date', 'currency')

    # Custom form to validate amount
    def save_model(self, request, obj, form, change):
        if obj.amount <= 0:
            self.message_user(request, "Amount must be greater than zero.", level="error")
        else:
            super().save_model(request, obj, form, change)

# FuelExpense Model with grouped filters
@admin.register(FuelExpense)
class FuelExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'date', 'amount', 'currency')
    search_fields = ('user__name', 'vehicle__license_plate')
    list_filter = (
        ('date', admin.DateFieldListFilter),  # Grouped by date
        'currency',
    )

# RouteOptimization Model with custom actions
@admin.register(RouteOptimization)
class RouteOptimizationAdmin(admin.ModelAdmin):
    list_display = ('start_location', 'end_location', 'optimized_route')
    search_fields = ('start_location', 'end_location')

    # Custom action to reset optimized routes
    @admin.action(description='Clear Optimized Routes')
    def clear_routes(self, request, queryset):
        queryset.update(optimized_route="Cleared")
        self.message_user(request, "Optimized routes have been cleared.")

    actions = [clear_routes]

# RoutePlan Model
@admin.register(RoutePlan)
class RoutePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'start_date', 'end_date')
    search_fields = ('user__name', 'vehicle__license_plate')
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
    search_fields = ('user__name', 'vehicle__license_plate', 'status')
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
# Preferences
@admin.register(UserPreferences)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'notifications_enabled')
    list_filter = ('theme', 'notifications_enabled')
    search_fields = ('user__username',)
#AiMaintenance
@admin.register(AiMaintenance)
class AiMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'maintenance_date')
    search_fields = ('vehicle', 'maintenance_date')
#AiPredictions
@admin.register(AiPredictions)
class AiPredictionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'prediction_type', 'prediction_date', 'prediction_result')
    search_fields = ('user', 'vehicle', 'prediction_result)
    list_filter = ('prediction_result', 'prediction_type', 'created date')
#Weather
@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('location', 'date', 'temperature')
#FleetAlert
@admin.register(FleetAlert)
class FleetAlertAdmin(admin.ModelAdmin):
    list-display = ('user', 'vehicle', 'alert_type', 'alert_message', 'created_at')
    search_fields = ('alert_type', 'vehicle', 'alert_message', 'created_at')
    


    
