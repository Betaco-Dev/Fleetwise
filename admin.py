from django.contrib import admin
from .models import (
    Admin, User, Vehicle, TrackingLog, MaintenanceSchedule, FuelExpense,
    RouteOptimization, RoutePlan, OtherExpense, DeliveryUpdate, AnalyticsReport, Currency
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

from django.contrib import admin
from .models import (
    Admin, User, Vehicle, TrackingLog, MaintenanceSchedule, FuelExpense,
    RouteOptimization, RoutePlan, OtherExpense, DeliveryUpdate, AnalyticsReport, Currency
)

# Admin Model
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

# User Model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('role', 'created_at')

# Vehicle Model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('type', 'license_plate', 'model', 'year')
    search_fields = ('license_plate', 'model')
    list_filter = ('type', 'year')

# TrackingLog Model
@admin.register(TrackingLog)
class TrackingLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'date_time', 'latitude', 'longitude')
    search_fields = ('user__name', 'vehicle__license_plate')
    list_filter = ('date_time',)

# MaintenanceSchedule Model
@admin.register(MaintenanceSchedule)
class MaintenanceScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'maintenance_date', 'description', 'amount', 'currency')
    search_fields = ('user__name', 'vehicle__license_plate', 'description')
    list_filter = ('maintenance_date', 'currency')

# FuelExpense Model
@admin.register(FuelExpense)
class FuelExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'date', 'amount', 'currency')
    search_fields = ('user__name', 'vehicle__license_plate')
    list_filter = ('date', 'currency')

# RouteOptimization Model
@admin.register(RouteOptimization)
class RouteOptimizationAdmin(admin.ModelAdmin):
    list_display = ('start_location', 'end_location', 'optimized_route')
    search_fields = ('start_location', 'end_location')

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
