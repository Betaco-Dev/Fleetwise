from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'license_number', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone')
