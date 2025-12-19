from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Allow read-only access to authenticated users.
    Write access is restricted to the owner.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        return obj.user == request.user
