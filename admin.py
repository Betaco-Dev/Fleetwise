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
