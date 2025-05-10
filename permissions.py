from rest_framework.permissions import BasePermission

class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to edit objects.
    Other users can only read.
    """
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True  # Allow read-only access for all users
        return request.user and request.user.is_staff  # Allow write access for admin users
