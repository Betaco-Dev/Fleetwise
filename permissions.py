from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to edit objects.
    
    - All users have read-only access (GET, HEAD, OPTIONS).
    - Only staff users have write access (POST, PUT, DELETE, etc.).
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow read-only access for all users
        return bool(request.user and request.user.is_staff)  # Allow write access for admin users

    def has_object_permission(self, request, view, obj):
        """
        Apply the same rule to object-level permissions.
        """
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
