from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnlyExceptRestricted(BasePermission):
    """
    Allows only admin (staff) users to write, edit, or delete.
    Non-admin users have read-only access except for restricted endpoints:
    (audit logs, analytics reports, tracking log, delivery updates) which are admin-only.
    """
    RESTRICTED_ENDPOINTS = [
        'auditlogs',         # e.g., /api/auditlogs/
        'analytics',         # e.g., /api/analytics/
        'trackinglog',       # e.g., /api/trackinglog/
        'deliveryupdates',   # e.g., /api/deliveryupdates/
    ]

    def _is_restricted(self, view):
        """
        Checks if the current view is a restricted endpoint.
        This method checks the view's basename or action for matching restricted endpoints.
        Adjust this logic based on your router/view naming conventions.
        """
        # Attempt to check view basename (DRF ViewSet)
        basename = getattr(view, 'basename', '').lower()
        if basename:
            for endpoint in self.RESTRICTED_ENDPOINTS:
                if endpoint in basename:
                    return True

        # Fallback: check URL name or view name
        view_name = getattr(view, '__class__', type(view)).__name__.lower()
        for endpoint in self.RESTRICTED_ENDPOINTS:
            if endpoint in view_name:
                return True

        return False

    def has_permission(self, request, view):
        if self._is_restricted(view):
            # Restricted endpoints: only admin for any action
            return bool(request.user and request.user.is_staff)
        if request.method in SAFE_METHODS:
            # All users can read for non-restricted endpoints
            return True
        # Only admin can write for non-restricted endpoints
        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        # Apply same rule at object level
        return self.has_permission(request, view)
